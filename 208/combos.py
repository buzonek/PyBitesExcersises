from itertools import combinations


def find_number_pairs(numbers, N=10):
    ret_list = list()
    for pair in combinations(numbers, 2):
        if sum(pair) == N:
            ret_list.append(pair)
    return ret_list
