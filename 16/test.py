from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    anniversaries = []
    date = PYBITES_BORN
    while True:
        date += timedelta(days=100)
        if date.year == 2020:
            break
        anniversaries.append(date)
    date = PYBITES_BORN
    while True:
        date += timedelta(days=365)
        if date.year == 2020:
            break
        anniversaries.append(date)
    anniversaries.sort()
    print(anniversaries)
gen_special_pybites_dates()