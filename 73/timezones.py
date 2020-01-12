import pytz
import datetime
MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    utc_ = pytz.utc
    utc_dt = utc_.localize(utc)
    for timezone in timezones:
        try:    
            tz = pytz.timezone(timezone)
        except Exception:
            raise ValueError
        new_time = utc_dt.astimezone(tz)
        if new_time.hour not in MEETING_HOURS:
            return False
    else:
        return True

