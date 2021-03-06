import csv
import os
from pathlib import Path
from urllib.request import urlretrieve

data = 'https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv'
tmp = Path(os.getenv("TMP", "/tmp"))
stats = tmp / 'bites.csv'

if not stats.exists():
    urlretrieve(data, stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """

    def _get_bite_no(bite):
        return bite['Bite'].split()[1].rstrip('.')

    with open(stats, encoding="utf-8-sig", ) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        sorted_bites = sorted([row for row in reader if row['Difficulty'] != 'None'],
                              key=lambda x: float(x['Difficulty']), reverse=True)
        return [_get_bite_no(bite) for bite in sorted_bites[:N]]


if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)