from itertools import cycle
import sys
from time import time, sleep

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \
STATE_TRANSITION_TIME = 0.1


def spinner(seconds):
    """Make a terminal loader/spinner animation using the imports aboveself.
       Takes seconds argument = time for the spinner to runself.
       Does not return anything, only prints to stdout."""
    repeats = seconds/STATE_TRANSITION_TIME
    char_gen = cycle(SPINNER_STATES)
    sys.stdout.flush()
    for i in range(round(repeats)):
        sys.stdout.write('\r' + next(char_gen))
        sleep(STATE_TRANSITION_TIME)
        sys.stdout.flush()


if __name__ == '__main__':
    spinner(1.2)