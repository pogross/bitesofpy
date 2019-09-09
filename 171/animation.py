from itertools import cycle
import sys
from time import time, sleep
import os

SPINNER_STATES = ["-", "\\", "|", "/"]  # had to escape \
STATE_TRANSITION_TIME = 0.1


def spinner(seconds):
    """Make a terminal loader/spinner animation using the imports aboveself.
       Takes seconds argument = time for the spinner to runself.
       Does not return anything, only prints to stdout."""
    end_time = time() + seconds
    states = cycle(SPINNER_STATES)
    while time() < end_time:
        sys.stdout.write(f"\r{next(states)}")
        sys.stdout.flush()
        sleep(STATE_TRANSITION_TIME)


if __name__ == "__main__":
    spinner(2)
