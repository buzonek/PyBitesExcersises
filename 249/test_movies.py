import os
import random
import string

import pytest

from movies import MovieDb

salt = ''.join(
    random.choice(string.ascii_lowercase) for i in range(20)
)
DB = os.path.join(os.getenv("TMP", "/tmp"), f'movies_{salt}.db')
# https://www.imdb.com/list/ls055592025/
DATA = [
    ("The Godfather", 1972, 9.2),
    ("The Shawshank Redemption", 1994, 9.3),
    ("Schindler's List", 1993, 8.9),
    ("Raging Bull", 1980, 8.2),
    ("Casablanca", 1942, 8.5),
    ("Citizen Kane", 1941, 8.3),
    ("Gone with the Wind", 1939, 8.1),
    ("The Wizard of Oz", 1939, 8),
    ("One Flew Over the Cuckoo's Nest", 1975, 8.7),
    ("Lawrence of Arabia", 1962, 8.3),
]
TABLE = 'movies'


@pytest.fixture
def db():
    db = MovieDb(DB, DATA, TABLE)
    db.init()
    yield db
    db.drop_table()


def test_db_query_default(db):
    ret_data = db.query()
    assert len(ret_data) == 10
    assert ret_data[0] == (1, "The Godfather", 1972, 9.2)
    assert ret_data[-1] == (10, "Lawrence of Arabia", 1962, 8.3)


@pytest.mark.parametrize('title,year, score_gt, expected', [
    ('Casablanca', None, None, [(5, "Casablanca", 1942, 8.5)]),
    (None, 1939, None, [(7, "Gone with the Wind", 1939, 8.1),
                        (8, "The Wizard of Oz", 1939, 8)]),
    (None, 2019, None, []),
    (None, None, 9.3, []),
    (None, None, 9.2, [(2, "The Shawshank Redemption", 1994, 9.3)]),

])
def test_db_query(db, title, year, score_gt, expected):
    assert db.query(title, year, score_gt)[1:] == expected


def test_db_add(db):
    movie = ("test_movie", "2019", 9.1)
    assert 11 == db.add(*movie)
    assert db.query(*movie) == (11, *movie)


def test_db_delete(db):
    db.delete(1)
    assert len(db.query()) == 9
    assert db.query("'The', 1972, 9.0") == []
