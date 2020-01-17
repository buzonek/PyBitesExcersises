from functools import wraps

MAX_RETRIES = 3


class MaxRetriesException(Exception):
    pass


def retry(func):
    """Complete this decorator, make sure
       you print the exception thrown"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        for i in range(MAX_RETRIES):
            try:
                return func(*args, **kwargs)
            except Exception as exc:
                print(exc)
        else:
            raise MaxRetriesException
    return wrapper
