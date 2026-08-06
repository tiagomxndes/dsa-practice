"""
We now need a way to show our LockedIn influencers the average (mean) follower count of the people they follow. This will help them know if they're following people who are more or less popular than them.
Complete the average_followers function.

    It should return the average of the given list of numbers.
    If the list is empty, it should return None.
"""


def average_followers(nums: list[int]) -> float | None:
    if not nums:
        return None

    return sum(nums) / len(nums)


print(average_followers([3, 6, 7]))
