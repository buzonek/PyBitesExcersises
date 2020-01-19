from collections import OrderedDict
from itertools import takewhile

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()
HONORS = OrderedDict(zip(scores, belts))


def get_belt(user_score):
    earned_scores = list(takewhile(lambda x: user_score >= x, scores))
    return HONORS[earned_scores[-1]] if earned_scores else None
