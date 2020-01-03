from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

Blog = namedtuple('Blog', blog.keys())


def dict2nt(dict_):
    return Blog._make(dict_.values())


def nt2json(nt):
    # helper function to convert datetime object to string
    # dumps cannot serialize datetime objects itself
    def datetime_to_str(o):
        if isinstance(o, datetime):
            return o.__str__()
    return json.dumps(nt._asdict(), default=datetime_to_str)