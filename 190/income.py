import os
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.request import urlretrieve
from collections import defaultdict

# import the countries xml file
tmp = Path(os.getenv("TMP", "/tmp"))
countries = tmp / 'countries.xml'

if not countries.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/countries.xml',
        countries
    )


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    ret_val = defaultdict(list)
    root = ET.parse(xml).getroot()
    ns = {'ns': 'http://www.worldbank.org'}
    for country in root:
        ret_val[country.find('ns:incomeLevel', ns).text].append(country.find('ns:name', ns).text)
    return ret_val
