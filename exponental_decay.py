"""
Assignment
Complete the decayed_followers function.
It calculates the final value of a quantity after a certain time has passed, given its initial value and a rate of decay. Return the remaining followers.
remaining_total = quantity * ( retention_rate ^ time )
The retention_rate is the opposite of fraction_lost_daily. If an influencer lost 0.2 (or 20%) of their followers each day, then the retention rate would be 0.8 (or 80%).
"""


def decayed_followers(
    initial_followers: int, fraction_lost_daily: float, days: int
) -> float:
    return initial_followers * ((1 - fraction_lost_daily) ** days)


print(decayed_followers(2, 0.8, 3))
