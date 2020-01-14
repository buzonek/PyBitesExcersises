import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = r'C:\Users\ematebu\Desktop\PythonProjects\PyBites\30'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    return_data = defaultdict(list)
    with open(MOVIE_DATA, 'r', encoding="utf8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            try:
                year = int(row['title_year'])
            except ValueError:
                continue
            if year < 1960:
                continue
            title = row['movie_title']
            score = float(row['imdb_score'])
            director = row['director_name']
            movie = Movie(title, year, score)
            return_data[director].append(movie)
    print(return_data)

get_movies_by_director()