"""A sample inline mapper app."""

from __future__ import annotations

from typing import TYPE_CHECKING, Generator

import singer_sdk.typing as th
from singer_sdk import _singerlib as singer
from singer_sdk.helpers._util import utc_now
from singer_sdk.mapper import PluginMapper
from singer_sdk.mapper_base import InlineMapper

from meltano_map_transform.countries import (
    COUNTRIES_DE,
    COUNTRIES_EN,
    COUNTRIES_FR,
    COUNTRY_CODES,
)

if TYPE_CHECKING:
    from pathlib import PurePath


class StreamTransform(InlineMapper):
    """A map transformer which implements the Stream Maps capability."""

    name = "meltano-map-transformer"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "country_map",
            th.ObjectType(
                additional_properties=th.CustomType(
                    {
                        "type": ["object", "null"],
                        "properties": {
                            "country_name": {"type": "string"},
                            "country_code": {"type": "string"},
                        },
                    }
                )
            ),
            required=False,
        ),
        th.Property(
            "stream_maps",
            th.ObjectType(
                additional_properties=th.CustomType(
                    {
                        "type": ["object", "string", "null"],
                        "properties": {
                            "__filter__": {"type": ["string", "null"]},
                            "__source__": {"type": ["string", "null"]},
                            "__alias__": {"type": ["string", "null"]},
                            "__else__": {
                                "type": ["string", "null"],
                                "enum": [None, "__NULL__"],
                            },
                            "__key_properties__": {
                                "type": ["array", "null"],
                                "items": {"type": "string"},
                            },
                        },
                        "additionalProperties": {"type": ["string", "null"]},
                    },
                ),
            ),
            required=False,
            description="Stream maps",
        ),
        th.Property(
            "flattening_enabled",
            th.BooleanType(),
            description=(
                "'True' to enable schema flattening and automatically expand nested "
                "properties."
            ),
        ),
        th.Property(
            "flattening_max_depth",
            th.IntegerType(),
            description="The max depth to flatten schemas.",
        ),
    ).to_dict()

    def __init__(
        self,
        *,
        config: dict | PurePath | str | list[PurePath | str] | None = None,
        parse_env_config: bool = False,
        validate_config: bool = True,
    ) -> None:
        """Create a new inline mapper.

        Args:
            config: Mapper configuration. Can be a dictionary, a single path to a
                configuration file, or a list of paths to multiple configuration
                files.
            parse_env_config: Whether to look for configuration values in environment
                variables.
            validate_config: True to require validation of config settings.
        """
        super().__init__(
            config=config,
            parse_env_config=parse_env_config,
            validate_config=validate_config,
        )

        self.mapper = PluginMapper(plugin_config=dict(self.config), logger=self.logger)

    def map_schema_message(
        self,
        message_dict: dict,
    ) -> Generator[singer.Message, None, None]:
        """Map a schema message according to config.

        Args:
            message_dict: A SCHEMA message JSON dictionary.

        Yields:
            Transformed schema messages.
        """
        self._assert_line_requires(message_dict, requires={"stream", "schema"})

        stream_id: str = message_dict["stream"]
        self.mapper.register_raw_stream_schema(
            stream_id,
            message_dict["schema"],
            message_dict.get("key_properties", []),
        )
        for stream_map in self.mapper.stream_maps[stream_id]:
            yield singer.SchemaMessage(
                stream_map.stream_alias,
                stream_map.transformed_schema,
                stream_map.transformed_key_properties,
                message_dict.get("bookmark_keys", []),
            )

    def map_record_message(
        self,
        message_dict: dict,
    ) -> Generator[singer.Message, None, None]:
        """Map a record message according to config.

        Args:
            message_dict: A RECORD message JSON dictionary.

        Yields:
            Transformed record messages.
        """
        self._assert_line_requires(message_dict, requires={"stream", "record"})

        stream_id: str = message_dict["stream"]
        for stream_map in self.mapper.stream_maps[stream_id]:
            mapped_record = stream_map.transform(message_dict["record"])
            if (
                mapped_record is not None
                and "country_map" in self.config
                and message_dict["stream"] in self.config["country_map"]
            ):
                mapped_record = self.map_country(
                    mapped_record,
                    self.config["country_map"][message_dict["stream"]],
                )
            if mapped_record is not None:
                yield singer.RecordMessage(
                    stream=stream_map.stream_alias,
                    record=mapped_record,
                    version=message_dict.get("version"),
                    time_extracted=utc_now(),
                )

    def map_country(self, mapped_dict: dict, country_map_config: dict) -> dict:
        """Map a record's country name according to config."""
        initial_country_name = mapped_dict.get(
            country_map_config.get("country_name", ""), ""
        ).strip()
        if not mapped_dict[country_map_config["country_code"]].isspace():
            country_code = mapped_dict[country_map_config["country_code"]]
            country_name = COUNTRY_CODES.get(country_code, initial_country_name)
            country_code = COUNTRIES_EN.get(
                country_name,
                COUNTRIES_DE.get(country_name, COUNTRIES_FR.get(country_name, "")),
            )
            if country_name == "":
                self.logger.info("Could not map country: country=%s", country_code)
        elif not mapped_dict[country_map_config["country_name"]].isspace():
            country_name = initial_country_name
            country_code = COUNTRIES_EN.get(
                country_name,
                COUNTRIES_DE.get(country_name, COUNTRIES_FR.get(country_name, "")),
            )
            country_name = COUNTRY_CODES.get(country_code, initial_country_name)
            if country_code == "":
                self.logger.info("Could not map country: country=%s", country_name)

        mapped_dict[country_map_config["country_name"]] = country_name
        mapped_dict[country_map_config["country_code"]] = country_code
        return mapped_dict

    def map_state_message(self, message_dict: dict) -> list[singer.Message]:
        """Do nothing to the message.

        Args:
            message_dict: A STATE message JSON dictionary.

        Returns:
            The same state message
        """
        return [singer.StateMessage(value=message_dict["value"])]

    def map_activate_version_message(
        self,
        message_dict: dict,
    ) -> Generator[singer.Message, None, None]:
        """Duplicate the message or alias the stream name as defined in configuration.

        Args:
            message_dict: An ACTIVATE_VERSION message JSON dictionary.

        Yields:
            An ACTIVATE_VERSION for each duplicated or aliased stream.
        """
        self._assert_line_requires(message_dict, requires={"stream", "version"})

        stream_id: str = message_dict["stream"]
        for stream_map in self.mapper.stream_maps[stream_id]:
            yield singer.ActivateVersionMessage(
                stream=stream_map.stream_alias,
                version=message_dict["version"],
            )
