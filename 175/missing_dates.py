import pandas as pd
from dateutil.rrule import rrule, DAILY
from datetime import date, datetime


def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    sorted_dates = sorted(dates)
    all_dates = list(x.date() for x in rrule(freq=DAILY, dtstart=sorted_dates[0], until=sorted_dates[-1]))
    return [x for x in all_dates if x not in dates]
