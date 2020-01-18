from datetime import date
from dateutil.rrule import rrule, YEARLY, SU


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    return list(rrule(YEARLY, dtstart=date(year, 1, 1), count=1, bymonth=5, byweekday=SU(+2)))[0].date()

