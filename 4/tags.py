import os
import re
from collections import Counter
import urllib.request

# prep

# this should work on pytest website
# tempfile = os.path.join('/tmp', 'feed')

# this works on my local windows machine
tempfile = os.path.join(os.getcwd(), 'feed.xml')
urllib.request.urlretrieve(
                            'https://bites-data.s3.us-east-2.amazonaws.com/feed',
                            tempfile)

with open(tempfile) as f:
    content = f.read().lower()


def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""

    # regexp matching everything between <category> and </category>
    pattern = "(?<=<category>).*?(?=<\/category>)"
    matches = re.findall(pattern, content)

    cnt = Counter()
    for match in matches:
        cnt[match] += 1

    return cnt.most_common(n)
