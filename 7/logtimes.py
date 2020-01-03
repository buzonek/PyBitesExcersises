from datetime import datetime, timedelta
import os
import re
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')


# this works on my local windows machine
#logfile = os.path.join(os.getcwd(), 'messages.log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()


def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    pattern = re.compile(r"(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})")
    match = pattern.search(line)
    matched_values = tuple(map(int, match.groups()))
    year, month, day, hour, minute, seconds = matched_values
    return datetime(year, month, day, hour, minute, seconds)


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdowns = []
    for line in loglines:
        if 'Shutdown initiated' in line:
            shutdowns.append(convert_to_datetime(line))

    return shutdowns[-1] - shutdowns[0]