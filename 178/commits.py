from collections import Counter
import os
import re
from urllib.request import urlretrieve

from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """

    def _extract_date(line):
        date_str = re.search(r'(?<=Date:).*?(?=[+-])', line)[0]
        return parse(date_str).strftime('%Y-%m')

    def _extract_changes(line):
        changes = re.findall(r'\d+(?= deletion| insertion)', line)
        return sum([int(x) for x in changes])

    with open(commits, 'r') as f:
        content = f.readlines()
    if year:
        year = str(year)
        content = [row for row in content if year in row]

    cnt = Counter()

    for row in content:
        date = _extract_date(row)
        changes = _extract_changes(row)
        cnt[date] += changes

    most_common = cnt.most_common()
    return most_common[-1][0], most_common[0][0]