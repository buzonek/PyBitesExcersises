import json
import re
from collections import namedtuple


def get_movie_data(files: list) -> list:
    movies_list = []
    for file in files:
        with open(file, 'r') as f:
            movies_list.append(json.load(f))


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        if 'Comedy' in movie['Genre']:
            return movie['Title']


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    Nominations = namedtuple('Nominations',['nominations', 'title'])
    max_nominations = Nominations(0, '')
    for movie in movies:
        nominations = int(re.findall(r"\d+(?= nominations.)", movie['Awards'])[0])
        if nominations > max_nominations.nominations:
            max_nominations = Nominations(nominations, movie['Title'])
    return max_nominations.title


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    MovieRuntime = namedtuple('Runtime', ['runtime', 'title'])
    max_runtime = MovieRuntime(0, '')
    for movie in movies:
        runtime = int(re.findall(r"\d+", movie['Runtime'])[0])
        if runtime > max_runtime.runtime:
            max_runtime = MovieRuntime(runtime, movie['Title'])
    return max_runtime.title

