from pathlib import Path
from urllib.request import urlretrieve
from collections import defaultdict
import xml.etree.ElementTree as ET

# import the countries xml file
tmp = Path("tmp")
countries = tmp / "countries.xml"

if not countries.exists():
    urlretrieve("https://bit.ly/2IzGKav", countries)


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    income_distribution = defaultdict(list)

    tree = ET.parse(countries)
    root = tree.getroot()

    for country in root.findall("{http://www.worldbank.org}country"):
        country_name = country.find("{http://www.worldbank.org}name").text
        income_lvl = country.find("{http://www.worldbank.org}incomeLevel").text
        income_distribution[income_lvl].append(country_name)

    return income_distribution
