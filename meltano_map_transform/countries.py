"""Country mappings. Source: https://github.com/geobase/countries/blob/master/countries/countries.json"""
from case_insensitive_dict import CaseInsensitiveDict

COUNTRY_CODES = {
    "AD": "Andorra",
    "AE": "United Arab Emirates",
    "AF": "Afghanistan",
    "AG": "Antigua and Barbuda",
    "AI": "Anguilla",
    "AL": "Albania",
    "AM": "Armenia",
    "AO": "Angola",
    "AQ": "Antarctica",
    "AR": "Argentina",
    "AS": "American Samoa",
    "AT": "Austria",
    "AU": "Australia",
    "AW": "Aruba",
    "AX": "Åland",
    "AZ": "Azerbaijan",
    "BA": "Bosnia and Herzegovina",
    "BB": "Barbados",
    "BD": "Bangladesh",
    "BE": "Belgium",
    "BF": "Burkina Faso",
    "BG": "Bulgaria",
    "BH": "Bahrain",
    "BI": "Burundi",
    "BJ": "Benin",
    "BL": "Saint Barthélemy",
    "BM": "Bermuda",
    "BN": "Brunei",
    "BO": "Bolivia",
    "BQ": "Bonaire",
    "BR": "Brazil",
    "BS": "Bahamas",
    "BT": "Bhutan",
    "BV": "Bouvet Island",
    "BW": "Botswana",
    "BY": "Belarus",
    "BZ": "Belize",
    "CA": "Canada",
    "CC": "Cocos [Keeling] Islands",
    "CD": "Democratic Republic of the Congo",
    "CF": "Central African Republic",
    "CG": "Republic of the Congo",
    "CH": "Switzerland",
    "CI": "Ivory Coast",
    "CK": "Cook Islands",
    "CL": "Chile",
    "CM": "Cameroon",
    "CN": "China",
    "CO": "Colombia",
    "CR": "Costa Rica",
    "CU": "Cuba",
    "CV": "Cape Verde",
    "CW": "Curacao",
    "CX": "Christmas Island",
    "CY": "Cyprus",
    "CZ": "Czechia",
    "DE": "Germany",
    "DJ": "Djibouti",
    "DK": "Denmark",
    "DM": "Dominica",
    "DO": "Dominican Republic",
    "DZ": "Algeria",
    "EC": "Ecuador",
    "EE": "Estonia",
    "EG": "Egypt",
    "EH": "Western Sahara",
    "ER": "Eritrea",
    "ES": "Spain",
    "ET": "Ethiopia",
    "FI": "Finland",
    "FJ": "Fiji",
    "FK": "Falkland Islands",
    "FM": "Micronesia",
    "FO": "Faroe Islands",
    "FR": "France",
    "GA": "Gabon",
    "GB": "United Kingdom",
    "GD": "Grenada",
    "GE": "Georgia",
    "GF": "French Guiana",
    "GG": "Guernsey",
    "GH": "Ghana",
    "GI": "Gibraltar",
    "GL": "Greenland",
    "GM": "Gambia",
    "GN": "Guinea",
    "GP": "Guadeloupe",
    "GQ": "Equatorial Guinea",
    "GR": "Greece",
    "GS": "South Georgia and the South Sandwich Islands",
    "GT": "Guatemala",
    "GU": "Guam",
    "GW": "Guinea-Bissau",
    "GY": "Guyana",
    "HK": "Hong Kong",
    "HM": "Heard Island and McDonald Islands",
    "HN": "Honduras",
    "HR": "Croatia",
    "HT": "Haiti",
    "HU": "Hungary",
    "ID": "Indonesia",
    "IE": "Ireland",
    "IL": "Israel",
    "IM": "Isle of Man",
    "IN": "India",
    "IO": "British Indian Ocean Territory",
    "IQ": "Iraq",
    "IR": "Iran",
    "IS": "Iceland",
    "IT": "Italy",
    "JE": "Jersey",
    "JM": "Jamaica",
    "JO": "Jordan",
    "JP": "Japan",
    "KE": "Kenya",
    "KG": "Kyrgyzstan",
    "KH": "Cambodia",
    "KI": "Kiribati",
    "KM": "Comoros",
    "KN": "Saint Kitts and Nevis",
    "KP": "North Korea",
    "KR": "South Korea",
    "KW": "Kuwait",
    "KY": "Cayman Islands",
    "KZ": "Kazakhstan",
    "LA": "Laos",
    "LB": "Lebanon",
    "LC": "Saint Lucia",
    "LI": "Liechtenstein",
    "LK": "Sri Lanka",
    "LR": "Liberia",
    "LS": "Lesotho",
    "LT": "Lithuania",
    "LU": "Luxembourg",
    "LV": "Latvia",
    "LY": "Libya",
    "MA": "Morocco",
    "MC": "Monaco",
    "MD": "Moldova",
    "ME": "Montenegro",
    "MF": "Saint Martin",
    "MG": "Madagascar",
    "MH": "Marshall Islands",
    "MK": "Macedonia",
    "ML": "Mali",
    "MM": "Myanmar",
    "MN": "Mongolia",
    "MO": "Macao",
    "MP": "Northern Mariana Islands",
    "MQ": "Martinique",
    "MR": "Mauritania",
    "MS": "Montserrat",
    "MT": "Malta",
    "MU": "Mauritius",
    "MV": "Maldives",
    "MW": "Malawi",
    "MX": "Mexico",
    "MY": "Malaysia",
    "MZ": "Mozambique",
    "NA": "Namibia",
    "NC": "New Caledonia",
    "NE": "Niger",
    "NF": "Norfolk Island",
    "NG": "Nigeria",
    "NI": "Nicaragua",
    "NL": "Netherlands",
    "NO": "Norway",
    "NP": "Nepal",
    "NR": "Nauru",
    "NU": "Niue",
    "NZ": "New Zealand",
    "OM": "Oman",
    "PA": "Panama",
    "PE": "Peru",
    "PF": "French Polynesia",
    "PG": "Papua New Guinea",
    "PH": "Philippines",
    "PK": "Pakistan",
    "PL": "Poland",
    "PM": "Saint Pierre and Miquelon",
    "PN": "Pitcairn Islands",
    "PR": "Puerto Rico",
    "PS": "Palestine",
    "PT": "Portugal",
    "PW": "Palau",
    "PY": "Paraguay",
    "QA": "Qatar",
    "RE": "Réunion",
    "RO": "Romania",
    "RS": "Serbia",
    "RU": "Russia",
    "RW": "Rwanda",
    "SA": "Saudi Arabia",
    "SB": "Solomon Islands",
    "SC": "Seychelles",
    "SD": "Sudan",
    "SE": "Sweden",
    "SG": "Singapore",
    "SH": "Saint Helena",
    "SI": "Slovenia",
    "SJ": "Svalbard and Jan Mayen",
    "SK": "Slovakia",
    "SL": "Sierra Leone",
    "SM": "San Marino",
    "SN": "Senegal",
    "SO": "Somalia",
    "SR": "Suriname",
    "SS": "South Sudan",
    "ST": "São Tomé and Príncipe",
    "SV": "El Salvador",
    "SX": "Sint Maarten",
    "SY": "Syria",
    "SZ": "Swaziland",
    "TC": "Turks and Caicos Islands",
    "TD": "Chad",
    "TF": "French Southern Territories",
    "TG": "Togo",
    "TH": "Thailand",
    "TJ": "Tajikistan",
    "TK": "Tokelau",
    "TL": "East Timor",
    "TM": "Turkmenistan",
    "TN": "Tunisia",
    "TO": "Tonga",
    "TR": "Turkey",
    "TT": "Trinidad and Tobago",
    "TV": "Tuvalu",
    "TW": "Taiwan",
    "TZ": "Tanzania",
    "UA": "Ukraine",
    "UG": "Uganda",
    "UM": "U.S. Minor Outlying Islands",
    "US": "United States",
    "UY": "Uruguay",
    "UZ": "Uzbekistan",
    "VA": "Vatican City",
    "VC": "Saint Vincent and the Grenadines",
    "VE": "Venezuela",
    "VG": "British Virgin Islands",
    "VI": "U.S. Virgin Islands",
    "VN": "Vietnam",
    "VU": "Vanuatu",
    "WF": "Wallis and Futuna",
    "WS": "Samoa",
    "XK": "Kosovo",
    "YE": "Yemen",
    "YT": "Mayotte",
    "ZA": "South Africa",
    "ZM": "Zambia",
    "ZW": "Zimbabwe",
}

COUNTRIES_EN = CaseInsensitiveDict[str, str](
    data={
        "Andorra": "AD",
        "United Arab Emirates": "AE",
        "Afghanistan": "AF",
        "Antigua and Barbuda": "AG",
        "Anguilla": "AI",
        "Albania": "AL",
        "Armenia": "AM",
        "Angola": "AO",
        "Antarctica": "AQ",
        "Argentina": "AR",
        "American Samoa": "AS",
        "Austria": "AT",
        "Australia": "AU",
        "Aruba": "AW",
        "Åland": "AX",
        "Azerbaijan": "AZ",
        "Bosnia and Herzegovina": "BA",
        "Barbados": "BB",
        "Bangladesh": "BD",
        "Belgium": "BE",
        "Burkina Faso": "BF",
        "Bulgaria": "BG",
        "Bahrain": "BH",
        "Burundi": "BI",
        "Benin": "BJ",
        "Saint Barthélemy": "BL",
        "Bermuda": "BM",
        "Brunei": "BN",
        "Bolivia": "BO",
        "Bonaire": "BQ",
        "Brazil": "BR",
        "Bahamas": "BS",
        "Bhutan": "BT",
        "Bouvet Island": "BV",
        "Botswana": "BW",
        "Belarus": "BY",
        "Belize": "BZ",
        "Canada": "CA",
        "Cocos [Keeling] Islands": "CC",
        "Democratic Republic of the Congo": "CD",
        "Central African Republic": "CF",
        "Republic of the Congo": "CG",
        "Switzerland": "CH",
        "Ivory Coast": "CI",
        "Cook Islands": "CK",
        "Chile": "CL",
        "Cameroon": "CM",
        "China": "CN",
        "Colombia": "CO",
        "Costa Rica": "CR",
        "Cuba": "CU",
        "Cape Verde": "CV",
        "Curacao": "CW",
        "Christmas Island": "CX",
        "Cyprus": "CY",
        "Czechia": "CZ",
        "Germany": "DE",
        "Djibouti": "DJ",
        "Denmark": "DK",
        "Dominica": "DM",
        "Dominican Republic": "DO",
        "Algeria": "DZ",
        "Ecuador": "EC",
        "Estonia": "EE",
        "Egypt": "EG",
        "Western Sahara": "EH",
        "Eritrea": "ER",
        "Spain": "ES",
        "Ethiopia": "ET",
        "Finland": "FI",
        "Fiji": "FJ",
        "Falkland Islands": "FK",
        "Micronesia": "FM",
        "Faroe Islands": "FO",
        "France": "FR",
        "Gabon": "GA",
        "United Kingdom": "GB",
        "Grenada": "GD",
        "Georgia": "GE",
        "French Guiana": "GF",
        "Guernsey": "GG",
        "Ghana": "GH",
        "Gibraltar": "GI",
        "Greenland": "GL",
        "Gambia": "GM",
        "Guinea": "GN",
        "Guadeloupe": "GP",
        "Equatorial Guinea": "GQ",
        "Greece": "GR",
        "South Georgia and the South Sandwich Islands": "GS",
        "Guatemala": "GT",
        "Guam": "GU",
        "Guinea-Bissau": "GW",
        "Guyana": "GY",
        "Hong Kong": "HK",
        "Heard Island and McDonald Islands": "HM",
        "Honduras": "HN",
        "Croatia": "HR",
        "Haiti": "HT",
        "Hungary": "HU",
        "Indonesia": "ID",
        "Ireland": "IE",
        "Israel": "IL",
        "Isle of Man": "IM",
        "India": "IN",
        "British Indian Ocean Territory": "IO",
        "Iraq": "IQ",
        "Iran": "IR",
        "Iceland": "IS",
        "Italy": "IT",
        "Jersey": "JE",
        "Jamaica": "JM",
        "Jordan": "JO",
        "Japan": "JP",
        "Kenya": "KE",
        "Kyrgyzstan": "KG",
        "Cambodia": "KH",
        "Kiribati": "KI",
        "Comoros": "KM",
        "Saint Kitts and Nevis": "KN",
        "North Korea": "KP",
        "South Korea": "KR",
        "Kuwait": "KW",
        "Cayman Islands": "KY",
        "Kazakhstan": "KZ",
        "Laos": "LA",
        "Lebanon": "LB",
        "Saint Lucia": "LC",
        "Liechtenstein": "LI",
        "Sri Lanka": "LK",
        "Liberia": "LR",
        "Lesotho": "LS",
        "Lithuania": "LT",
        "Luxembourg": "LU",
        "Latvia": "LV",
        "Libya": "LY",
        "Morocco": "MA",
        "Monaco": "MC",
        "Moldova": "MD",
        "Montenegro": "ME",
        "Saint Martin": "MF",
        "Madagascar": "MG",
        "Marshall Islands": "MH",
        "Macedonia": "MK",
        "Mali": "ML",
        "Myanmar": "MM",
        "Mongolia": "MN",
        "Macao": "MO",
        "Northern Mariana Islands": "MP",
        "Martinique": "MQ",
        "Mauritania": "MR",
        "Montserrat": "MS",
        "Malta": "MT",
        "Mauritius": "MU",
        "Maldives": "MV",
        "Malawi": "MW",
        "Mexico": "MX",
        "Malaysia": "MY",
        "Mozambique": "MZ",
        "Namibia": "NA",
        "New Caledonia": "NC",
        "Niger": "NE",
        "Norfolk Island": "NF",
        "Nigeria": "NG",
        "Nicaragua": "NI",
        "Netherlands": "NL",
        "Norway": "NO",
        "Nepal": "NP",
        "Nauru": "NR",
        "Niue": "NU",
        "New Zealand": "NZ",
        "Oman": "OM",
        "Panama": "PA",
        "Peru": "PE",
        "French Polynesia": "PF",
        "Papua New Guinea": "PG",
        "Philippines": "PH",
        "Pakistan": "PK",
        "Poland": "PL",
        "Saint Pierre and Miquelon": "PM",
        "Pitcairn Islands": "PN",
        "Puerto Rico": "PR",
        "Palestine": "PS",
        "Portugal": "PT",
        "Palau": "PW",
        "Paraguay": "PY",
        "Qatar": "QA",
        "Réunion": "RE",
        "Romania": "RO",
        "Serbia": "RS",
        "Russia": "RU",
        "Rwanda": "RW",
        "Saudi Arabia": "SA",
        "Solomon Islands": "SB",
        "Seychelles": "SC",
        "Sudan": "SD",
        "Sweden": "SE",
        "Singapore": "SG",
        "Saint Helena": "SH",
        "Slovenia": "SI",
        "Svalbard and Jan Mayen": "SJ",
        "Slovakia": "SK",
        "Sierra Leone": "SL",
        "San Marino": "SM",
        "Senegal": "SN",
        "Somalia": "SO",
        "Suriname": "SR",
        "South Sudan": "SS",
        "São Tomé and Príncipe": "ST",
        "El Salvador": "SV",
        "Sint Maarten": "SX",
        "Syria": "SY",
        "Swaziland": "SZ",
        "Turks and Caicos Islands": "TC",
        "Chad": "TD",
        "French Southern Territories": "TF",
        "Togo": "TG",
        "Thailand": "TH",
        "Tajikistan": "TJ",
        "Tokelau": "TK",
        "East Timor": "TL",
        "Turkmenistan": "TM",
        "Tunisia": "TN",
        "Tonga": "TO",
        "Turkey": "TR",
        "Trinidad and Tobago": "TT",
        "Tuvalu": "TV",
        "Taiwan": "TW",
        "Tanzania": "TZ",
        "Ukraine": "UA",
        "Uganda": "UG",
        "U.S. Minor Outlying Islands": "UM",
        "United States": "US",
        "Uruguay": "UY",
        "Uzbekistan": "UZ",
        "Vatican City": "VA",
        "Saint Vincent and the Grenadines": "VC",
        "Venezuela": "VE",
        "British Virgin Islands": "VG",
        "U.S. Virgin Islands": "VI",
        "Vietnam": "VN",
        "Vanuatu": "VU",
        "Wallis and Futuna": "WF",
        "Samoa": "WS",
        "Kosovo": "XK",
        "Yemen": "YE",
        "Mayotte": "YT",
        "South Africa": "ZA",
        "Zambia": "ZM",
        "Zimbabwe": "ZW",
    }
)


COUNTRIES_DE = CaseInsensitiveDict[str, str](
    data={
        "Andorra": "AD",
        "Vereinigte Arabische Emirate": "AE",
        "Afghanistan": "AF",
        "Antigua und Barbuda": "AG",
        "Anguilla": "AI",
        "Albanien": "AL",
        "Armenien": "AM",
        "Angola": "AO",
        "Antarktis": "AQ",
        "Argentinien": "AR",
        "Amerikanisch-Samoa": "AS",
        "Österreich": "AT",
        "Australien": "AU",
        "Aruba": "AW",
        "Alandinseln": "AX",
        "Aserbaidschan": "AZ",
        "Bosnien und Herzegowina": "BA",
        "Barbados": "BB",
        "Bangladesch": "BD",
        "Belgien": "BE",
        "Burkina Faso": "BF",
        "Bulgarien": "BG",
        "Bahrain": "BH",
        "Burundi": "BI",
        "Benin": "BJ",
        "St. Barthélemy": "BL",
        "Bermuda": "BM",
        "Brunei": "BN",
        "Bolivien": "BO",
        "Bonaire": "BQ",
        "Brasilien": "BR",
        "Bahamas": "BS",
        "Bhutan": "BT",
        "Bouvetinsel": "BV",
        "Botswana": "BW",
        "Weißrussland": "BY",
        "Belize": "BZ",
        "Kanada": "CA",
        "Kokosinseln": "CC",
        "Demokratische Republik Kongo": "CD",
        "Zentralafrikanische Republik": "CF",
        "Kongo (Republik Kongo)": "CG",
        "Schweiz": "CH",
        "Elfenbeinküste": "CI",
        "Cookinseln": "CK",
        "Chile": "CL",
        "Kamerun": "CM",
        "China": "CN",
        "Kolumbien": "CO",
        "Costa Rica": "CR",
        "Kuba": "CU",
        "Kap Verde": "CV",
        "Curaçao": "CW",
        "Weihnachtsinsel": "CX",
        "Zypern": "CY",
        "Tschechien": "CZ",
        "Deutschland": "DE",
        "Dschibuti": "DJ",
        "Dänemark": "DK",
        "Dominica": "DM",
        "Dominikanische Republik": "DO",
        "Algerien": "DZ",
        "Ecuador": "EC",
        "Estland": "EE",
        "Ägypten": "EG",
        "Westsahara": "EH",
        "Eritrea": "ER",
        "Spanien": "ES",
        "Äthiopien": "ET",
        "Finnland": "FI",
        "Fidschi": "FJ",
        "Falklandinseln": "FK",
        "Mikronesien": "FM",
        "Färöer-Inseln": "FO",
        "Frankreich": "FR",
        "Gabun": "GA",
        "Vereinigtes Königreich": "GB",
        "Grenada": "GD",
        "Georgien": "GE",
        "Französisch-Guayana": "GF",
        "Guernsey": "GG",
        "Ghana": "GH",
        "Gibraltar": "GI",
        "Grönland": "GL",
        "Gambia": "GM",
        "Guinea": "GN",
        "Guadeloupe": "GP",
        "Äquatorialguinea": "GQ",
        "Griechenland": "GR",
        "Südgeorgien und die Südlichen Sandwichinseln": "GS",
        "Guatemala": "GT",
        "Guam": "GU",
        "Guinea-Bissau": "GW",
        "Guyana": "GY",
        "Hongkong": "HK",
        "Heard- und McDonald-Inseln": "HM",
        "Honduras": "HN",
        "Kroatien": "HR",
        "Haiti": "HT",
        "Ungarn": "HU",
        "Indonesien": "ID",
        "Irland": "IE",
        "Israel": "IL",
        "Insel Man": "IM",
        "Indien": "IN",
        "Britisches Territorium im Indischen Ozean": "IO",
        "Irak": "IQ",
        "Iran (Islamische Republik)": "IR",
        "Island": "IS",
        "Italien": "IT",
        "Jersey": "JE",
        "Jamaika": "JM",
        "Jordanien": "JO",
        "Japan": "JP",
        "Kenia": "KE",
        "Kirgistan": "KG",
        "Kambodscha": "KH",
        "Kiribati": "KI",
        "Komoren": "KM",
        "Saint Kitts und Nevis": "KN",
        "Nordkorea": "KP",
        "Südkorea": "KR",
        "Kuwait": "KW",
        "Kaimaninseln": "KY",
        "Kasachstan": "KZ",
        "Laos": "LA",
        "Libanon": "LB",
        "St. Lucia": "LC",
        "Liechtenstein": "LI",
        "Sri Lanka": "LK",
        "Liberia": "LR",
        "Lesotho": "LS",
        "Litauen": "LT",
        "Luxemburg": "LU",
        "Lettland": "LV",
        "Libyen": "LY",
        "Marokko": "MA",
        "Monaco": "MC",
        "Moldau (Republik Moldau)": "MD",
        "Montenegro": "ME",
        "St. Martin": "MF",
        "Madagaskar": "MG",
        "Marshall-Inseln": "MH",
        "Mazedonien": "MK",
        "Mali": "ML",
        "Birma (Myanmar)": "MM",
        "Mongolei": "MN",
        "Macau": "MO",
        "Nördliche Marianen": "MP",
        "Martinique": "MQ",
        "Mauretanien": "MR",
        "Montserrat": "MS",
        "Malta": "MT",
        "Mauritius": "MU",
        "Malediven": "MV",
        "Malawi": "MW",
        "Mexiko": "MX",
        "Malaysien": "MY",
        "Mosambik": "MZ",
        "Namibia": "NA",
        "Neukaledonien": "NC",
        "Niger": "NE",
        "Norfolkinsel": "NF",
        "Nigeria": "NG",
        "Nikaragua": "NI",
        "Niederlande": "NL",
        "Norwegen": "NO",
        "Nepal": "NP",
        "Nauru": "NR",
        "Niue": "NU",
        "Neuseeland": "NZ",
        "Oman": "OM",
        "Panama": "PA",
        "Peru": "PE",
        "Französisch-Polynesien": "PF",
        "Papua-Neuguinea": "PG",
        "Philippinen": "PH",
        "Pakistan": "PK",
        "Polen": "PL",
        "St. Pierre und Miquelon": "PM",
        "Pitcairn": "PN",
        "Puerto Rico": "PR",
        "Palästinensische Autonomiegebiete": "PS",
        "Portugal": "PT",
        "Palau": "PW",
        "Paraguay": "PY",
        "Katar": "QA",
        "Réunion": "RE",
        "Rumänien": "RO",
        "Serbien": "RS",
        "Russland": "RU",
        "Ruanda": "RW",
        "Saudi-Arabien": "SA",
        "Solomon-Inseln": "SB",
        "Seychellen": "SC",
        "Sudan": "SD",
        "Schweden": "SE",
        "Singapur": "SG",
        "St. Helena": "SH",
        "Slowenien": "SI",
        "Svalbard und Jan Mayen": "SJ",
        "Slowakei": "SK",
        "Sierra Leone": "SL",
        "San Marino": "SM",
        "Senegal": "SN",
        "Somalia": "SO",
        "Suriname": "SR",
        "Südsudan": "SS",
        "Sao Tomé und Principe": "ST",
        "El Salvador": "SV",
        "Sint Maarten": "SX",
        "Syrien": "SY",
        "Swasiland": "SZ",
        "Turks- und Caicosinseln": "TC",
        "Tschad": "TD",
        "Französische Süd- und Antarktisgebiete": "TF",
        "Togo": "TG",
        "Thailand": "TH",
        "Tadschikistan": "TJ",
        "Tokelau": "TK",
        "Timor-Leste": "TL",
        "Turkmenistan": "TM",
        "Tunesien": "TN",
        "Tonga": "TO",
        "Türkei": "TR",
        "Trinidad und Tobago": "TT",
        "Tuwalu": "TV",
        "Taiwan": "TW",
        "Tansania": "TZ",
        "Ukraine": "UA",
        "Uganda": "UG",
        "Amerikanisch-Ozeanien": "UM",
        "USA": "US",
        "Uruguay": "UY",
        "Usbekistan": "UZ",
        "Staat der Vatikanstadt": "VA",
        "St. Vincent und die Grenadinen": "VC",
        "Venezuela": "VE",
        "Britische Jungferninseln": "VG",
        "Amerikanische Jungferninseln": "VI",
        "Vietnam": "VN",
        "Vanuatu": "VU",
        "Wallis und Futuna": "WF",
        "Samoa": "WS",
        "Kosovo": "XK",
        "Jemen": "YE",
        "Mayotte": "YT",
        "Südafrika": "ZA",
        "Sambia": "ZM",
        "Simbabwe": "ZW",
    }
)

COUNTRIES_FR = CaseInsensitiveDict[str, str](
    data={
        "Andorre": "AD",
        "Émirats Arabes Unis": "AE",
        "Afghanistan": "AF",
        "Antigua et Barbuda": "AG",
        "Anguilla": "AI",
        "Albanie": "AL",
        "Arménie": "AM",
        "Angola": "AO",
        "Antarctique": "AQ",
        "Argentine": "AR",
        "Samoa américaines": "AS",
        "Autriche": "AT",
        "Australie": "AU",
        "Aruba": "AW",
        "Îles Åland": "AX",
        "Azerbaïdjan": "AZ",
        "Bosnie-Herzégovine": "BA",
        "Barbade": "BB",
        "Bangladesh": "BD",
        "Belgique": "BE",
        "Burkina Faso": "BF",
        "Bulgarie": "BG",
        "Bahreïn": "BH",
        "Burundi": "BI",
        "Bénin": "BJ",
        "Saint-Barthélémy": "BL",
        "Bermudes": "BM",
        "Brunéi Darussalam": "BN",
        "Bolivie": "BO",
        "Bonaire, Saint-Eustache et Saba": "BQ",
        "Brésil": "BR",
        "Bahamas": "BS",
        "Bhutan": "BT",
        "Île Bouvet": "BV",
        "Botswana": "BW",
        "Biélorussie": "BY",
        "Belize": "BZ",
        "Canada": "CA",
        "Îles Cocos": "CC",
        "RDC": "CD",
        "Centrafrique": "CF",
        "Congo-Brazzaville": "CG",
        "Suisse": "CH",
        "Côte d'Ivoire": "CI",
        "Îles Cook": "CK",
        "Chili": "CL",
        "Cameroun": "CM",
        "Chine": "CN",
        "Colombie": "CO",
        "Costa Rica": "CR",
        "Cuba": "CU",
        "Cap-Vert": "CV",
        "Curaçao": "CW",
        "Île Christmas": "CX",
        "Chypre": "CY",
        "République tchèque": "CZ",
        "Allemagne": "DE",
        "Djibouti": "DJ",
        "Danemark": "DK",
        "Dominique": "DM",
        "République Dominicaine": "DO",
        "Algérie": "DZ",
        "Équateur": "EC",
        "Estonie": "EE",
        "Égypte": "EG",
        "Sahara Occidental": "EH",
        "Érythrée": "ER",
        "Espagne": "ES",
        "Éthiopie": "ET",
        "Finlande": "FI",
        "Fidji": "FJ",
        "Îles Malouines": "FK",
        "Micronésie": "FM",
        "Îles Féroé": "FO",
        "France": "FR",
        "Gabon": "GA",
        "Royaume-Uni": "GB",
        "Grenade": "GD",
        "Géorgie": "GE",
        "Guyane": "GF",
        "Guernesey": "GG",
        "Ghana": "GH",
        "Gibraltar": "GI",
        "Groenland": "GL",
        "Gambie": "GM",
        "Guinée": "GN",
        "Guadeloupe": "GP",
        "Guinée équatoriale": "GQ",
        "Grèce": "GR",
        "Géorgie du Sud et les îles Sandwich du Sud": "GS",
        "Guatemala": "GT",
        "Guam": "GU",
        "Guinée-Bissau": "GW",
        "Guyana": "GY",
        "Hong Kong": "HK",
        "Île Heard et îles McDonald": "HM",
        "Honduras": "HN",
        "Croatie": "HR",
        "Haïti": "HT",
        "Hongrie": "HU",
        "Indonésie": "ID",
        "Irlande": "IE",
        "Israël": "IL",
        "Île de Man": "IM",
        "Inde": "IN",
        "Territoire britannique de l'océan Indien": "IO",
        "Irak": "IQ",
        "Iran": "IR",
        "Islande": "IS",
        "Italie": "IT",
        "Jersey": "JE",
        "Jamaïque": "JM",
        "Jordanie": "JO",
        "Japon": "JP",
        "Kenya": "KE",
        "Kirghizistan": "KG",
        "Cambodge": "KH",
        "Kiribati": "KI",
        "Comores": "KM",
        "Saint-Christophe-et-Niévès": "KN",
        "Corée du Nord": "KP",
        "Corée du Sud": "KR",
        "Koweït": "KW",
        "Îles Caïmans": "KY",
        "Kazakhstan": "KZ",
        "Laos": "LA",
        "Liban": "LB",
        "Sainte-Lucie": "LC",
        "Liechtenstein": "LI",
        "Sri Lanka": "LK",
        "Liberia": "LR",
        "Lesotho": "LS",
        "Lituanie": "LT",
        "Luxembourg": "LU",
        "Lettonie": "LV",
        "Libye": "LY",
        "Maroc": "MA",
        "Monaco": "MC",
        "Moldavie": "MD",
        "Monténégro": "ME",
        "Saint-Martin": "SX",
        "Madagascar": "MG",
        "Îles Marshall": "MH",
        "Macédoine": "MK",
        "Mali": "ML",
        "Myanmar": "MM",
        "Mongolie": "MN",
        "Macao": "MO",
        "Îles Mariannes du Nord": "MP",
        "Martinique": "MQ",
        "Mauritanie": "MR",
        "Montserrat": "MS",
        "Malte": "MT",
        "Maurice": "MU",
        "Maldives": "MV",
        "Malawi": "MW",
        "Mexique": "MX",
        "Malaisie": "MY",
        "Mozambique": "MZ",
        "Namibie": "NA",
        "Nouvelle-Calédonie": "NC",
        "Niger": "NE",
        "Île Norfolk": "NF",
        "Nigeria": "NG",
        "Nicaragua": "NI",
        "Pays-Bas": "NL",
        "Norvège": "NO",
        "Népal": "NP",
        "Nauru": "NR",
        "Nioué": "NU",
        "Nouvelle-Zélande": "NZ",
        "Oman": "OM",
        "Panama": "PA",
        "Pérou": "PE",
        "Polynésie Française": "PF",
        "Papouasie-Nouvelle Guinée": "PG",
        "Philippines": "PH",
        "Pakistan": "PK",
        "Pologne": "PL",
        "Saint-Pierre et Miquelon": "PM",
        "Pitcairn": "PN",
        "Porto Rico": "PR",
        "Territoire palestinien": "PS",
        "Portugal": "PT",
        "Palaos": "PW",
        "Paraguay": "PY",
        "Qatar": "QA",
        "Réunion": "RE",
        "Roumanie": "RO",
        "Serbie": "RS",
        "Russie": "RU",
        "Rwanda": "RW",
        "Arabie saoudite": "SA",
        "Îles Salomon": "SB",
        "Seychelles": "SC",
        "Soudan": "SD",
        "Suède": "SE",
        "Singapour": "SG",
        "Sainte-Hélène": "SH",
        "Slovénie": "SI",
        "Svalbard et Île Jan Mayen": "SJ",
        "Slovaquie": "SK",
        "Sierra Leone": "SL",
        "Saint-Marin": "SM",
        "Sénégal": "SN",
        "Somalie": "SO",
        "Surinam": "SR",
        "Sud-Soudan": "SS",
        "São Tomé-et-Príncipe": "ST",
        "Salvador": "SV",
        "Syrie": "SY",
        "Swaziland": "SZ",
        "Îles Turques-et-Caïques": "TC",
        "Tchad": "TD",
        "Terres australes françaises": "TF",
        "République Togolaise": "TG",
        "Thaïlande": "TH",
        "Tadjikistan": "TJ",
        "Tokelau": "TK",
        "Timor Oriental": "TL",
        "Turkménistan": "TM",
        "Tunisie": "TN",
        "Tonga": "TO",
        "Turquie": "TR",
        "Trinidad et Tobago": "TT",
        "Tuvalu": "TV",
        "Taïwan": "TW",
        "Tanzanie": "TZ",
        "Ukraine": "UA",
        "Ouganda": "UG",
        "Îles mineures éloignées des États-Unis": "UM",
        "États-Unis": "US",
        "Uruguay": "UY",
        "Ouzbékistan": "UZ",
        "Vatican": "VA",
        "Saint-Vincent-et-les Grenadines": "VC",
        "Vénézuéla": "VE",
        "Îles Vierges": "VG",
        "Îles Vierges des États-Unis": "VI",
        "Vietnam": "VN",
        "Vanuatu": "VU",
        "Wallis-et-Futuna": "WF",
        "Samoa": "WS",
        "Kosovo": "XK",
        "Yémen": "YE",
        "Mayotte": "YT",
        "Afrique du Sud": "ZA",
        "Zambie": "ZM",
        "Zimbabwe": "ZW",
    }
)
