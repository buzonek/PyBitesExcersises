import requests
from collections import defaultdict, Counter

STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    if cap == 'n/a':
        return 0
    else:
        cap = cap.lstrip('$')
        if 'M' in cap:
            return float(cap.rstrip('M'))
        elif 'B' in cap:
            return float(cap.rstrip('B')) * 1000
        else:
            return float(cap)


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    total_cap = 0
    for line in data:
        if line['industry'] == industry:
            total_cap += _cap_str_to_mln_float(line['cap'])
    return round(total_cap, 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    symbols_cap = defaultdict(float)
    for line in data:
        symbols_cap[line['symbol']] += _cap_str_to_mln_float(line['cap'])
    return max([(k, v) for k, v in symbols_cap.items()], key=lambda x: x[1])[0]


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    cnt = Counter([row['sector'] for row in data if row['sector'] != 'n/a'])
    return cnt.most_common()[0][0], cnt.most_common()[-1][0]

