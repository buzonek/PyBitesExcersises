from pcc_stats import diehard_pybites, Stats


def test_diehard_pybites():
    res = diehard_pybites()
    print(res)
    assert res == Stats(user='clamytoe', challenge=('01', 7))
