import os
import urllib.request
from collections import defaultdict

TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'

urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)

with open(SAFARI_LOGS) as f:
    content = f.readlines()


def create_chart():
    chart_data = defaultdict(list)
    for line_no, line in enumerate(content):
        if 'sending to slack channel' in line:
            day = line.split()[0]
            if 'python' in content[line_no - 1].lower():
                char = PY_BOOK
            else:
                char = OTHER_BOOK
            chart_data[day].append(char)
    print('\n'.join([k + ' ' + ''.join(v) for k, v in chart_data.items()]))

