import os
import re
import urllib.request
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


with open(stopwords_file) as f:
    stopwords = f.read().splitlines()

pattern = re.compile(r'\W+', re.UNICODE)
words_counter = Counter()


def get_harry_most_common_word():
    with open(harry_text, encoding='utf8') as f:
        for line in f:
            # skip blink lines
            line = line.strip()
            if line == "":
                continue
            # convert to lower and split line into words
            words = line.lower().split()
            # get rid of non-alpha characters by replacing them using regexp
            alpha_words = [pattern.sub('', word) for word in words]
            words_counter.update([word for word in alpha_words if word not in stopwords and word])
    return words_counter.most_common(1)
