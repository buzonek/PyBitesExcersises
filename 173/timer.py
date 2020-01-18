from datetime import datetime, timedelta
import re

NOW = datetime(year=2019, month=2, day=6,
               hour=22, minute=0, second=0)


def add_todo(delay_time: str, task: str,
             start_time: datetime = NOW) -> str:
    """
    Parse out the time unit from the passed in delay_time str:
    - 30d = 30 days
    - 1h 10m = 1 hour and 10 min
    - 5m 3s = 5 min and 3 seconds
    - 45 or 45s = 45 seconds

    Return the task and planned time which is calculated from
    provided start_time (here default = NOW):
    """
    mapping = {'d': 'days', 'h': 'hours', 'm': 'minutes', 's': 'seconds', '': 'seconds'}
    tmd_values = {'days': 0, 'hours': 0, 'minutes': 0, 'seconds': 0}
    matches = re.finditer(r'(\d+)(\w*)', delay_time)
    for match in matches:
        unit = mapping[match.group(2)]
        tmd_values[unit] = int(match.group(1))
    future_date = start_time + timedelta(**tmd_values)
    return f'{task} @ {future_date.strftime("%Y-%m-%d %H:%M:%S")}'

