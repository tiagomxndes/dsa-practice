"""
Assignment

Another one of the CEO's posts went viral, and LockedIn's servers can't keep up. The team needs you to implement exponential backoff so that requests wait longer and longer between retries.

Complete the backoff_delays function. It's a generator function that yields retry delays in seconds.

    Initialize the delay value at base seconds.
    Use a while loop to repeat indefinitely. In each iteration:
        Yield the current delay.
        Double the delay for the next iteration.

"""


def backoff_delays(base: int):
    delay = base

    while True:
        yield delay
        delay *= 2
