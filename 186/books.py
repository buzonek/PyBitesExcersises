from datetime import datetime

from dateutil.parser import parse

# work with a static date for tests, real use = datetime.now()
NOW = datetime(2019, 3, 17, 16, 28, 42, 966663)
WEEKS_PER_YEAR = 52


def get_number_books_read(books_per_year_goal: int,
                          at_date: str = None) -> int:
    """Based on books_per_year_goal and at_date, return the
       number of books that should have been read.
       If books_per_year_goal negative or 0, or at_date is in the
       past, raise a ValueError."""
    dt = NOW if not at_date else parse(at_date)
    if books_per_year_goal <= 0 or dt < NOW:
        raise ValueError
    week_no = dt.isocalendar()[1]
    return int(week_no/WEEKS_PER_YEAR*books_per_year_goal)