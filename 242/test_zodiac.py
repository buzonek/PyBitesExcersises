import json
import os
from datetime import datetime
from pathlib import Path
from urllib.request import urlretrieve

import pytest

from zodiac import (get_signs, get_sign_with_most_famous_people,
                    signs_are_mutually_compatible, get_sign_by_date)

# original source: https://zodiacal.herokuapp.com/api
URL = "https://bites-data.s3.us-east-2.amazonaws.com/zodiac.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "zodiac.json")


@pytest.fixture(scope='module')
def signs():
    if not PATH.exists():
        urlretrieve(URL, PATH)
    with open(PATH) as f:
        data = json.loads(f.read())
    return get_signs(data)


def test_get_sign_with_most_famous_people(signs):
    most_famous = get_sign_with_most_famous_people(signs)
    assert most_famous == ('Scorpio', 35)
    assert most_famous.__class__.__name__ == "Sign"


def test_signs_are_mutally_compatible(signs):
    assert signs_are_mutually_compatible(signs, "Ares", "Leo")
    assert signs_are_mutually_compatible(signs, "Leo", "Ares")


def test_get_sign_by_date(signs):
    date1 = datetime(2019, 2, 22)
    date2 = datetime(2019, 12, 31)
    assert get_sign_by_date(signs, date1) == "Pisces"
    assert get_sign_by_date(signs, date2) == "Capricorn"
