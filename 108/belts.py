from collections import namedtuple

BeltStats = namedtuple('BeltStats', 'score ninjas')

ninja_belts = {'yellow': BeltStats(50, 11),
               'orange': BeltStats(100, 7),
               'green': BeltStats(175, 1),
               'blue': BeltStats(250, 5)}


def get_total_points(belts=ninja_belts):
    if belts:
        _sum = 0
        for belt in belts.values():
            _sum += belt.score * belt.ninjas
    return _sum


def test_get_total_points_given_belts():
    assert get_total_points(ninja_belts) == 2675


def test_get_total_points_more_belts():
    more_belts = dict(brown=BeltStats(400, 2),
                      black=BeltStats(600, 5))

    # this way to dict merge is >= 3.5 (PEP 448)
    ninja_belts_updated = {**ninja_belts, **more_belts}

    assert get_total_points(ninja_belts_updated) == 6475


test_get_total_points_given_belts()
test_get_total_points_more_belts()