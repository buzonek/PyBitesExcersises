import string
from itertools import cycle, chain


def sequence_generator():
     return cycle(chain.from_iterable(zip(range(1, 27), string.ascii_uppercase)))
