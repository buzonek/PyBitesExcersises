from functools import wraps


def int_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if any(type(x) == int for x in args):
            raise TypeError
        if all(x > 0 for x in args):
            raise ValueError
        func(*args, **kwargs)
    return wrapper
