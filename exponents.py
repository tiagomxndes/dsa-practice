"""
Complete the get_estimated_spread function by implementing the formula above.
The only input is audiences_followers, which is a list of the follower counts of all the followers the author has.
Return the estimated spread. If the audiences_followers list is empty, return 0.
"""


def get_estimated_spread(audiences_followers: list[int]) -> float:
    if not audiences_followers:
        return 0

    average_audience_followers = sum(audiences_followers) / len(audiences_followers)

    return average_audience_followers * (len(audiences_followers) ** 1.2)


audiences_followers = [2, 3, 2, 9]
print(get_estimated_spread(audiences_followers))
print(get_estimated_spread([2, 3, 2, 19]))
print(get_estimated_spread([]))
