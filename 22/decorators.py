from functools import wraps


def make_html(element):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return '<{0}>{1}</{0}>'.format(element, func(*args, **kwargs))
        return wrapper
    return decorator
