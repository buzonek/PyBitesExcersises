from itertools import accumulate


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    def mean(a, b):
        return round((a + b)/2, 2)
    return list(accumulate(sequence, func=mean))
