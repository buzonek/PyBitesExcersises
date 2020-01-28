import re


def get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    weekdays = {}
    calendar_lines = calendar_output.splitlines()
    week_days = calendar_lines[1].split(' ')
    for week in calendar_lines[2:]:
        days_numbers = re.findall(r'[ \d]{2,3}', week)
        for index, day_no in enumerate(days_numbers):
            day_no = day_no.strip()
            if day_no:
                weekdays[int(day_no)] = week_days[index]
    return weekdays
