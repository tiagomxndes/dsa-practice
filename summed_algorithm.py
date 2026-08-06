"""
Assignment
For the LockedIn influencer dashboard, we need to calculate the total reach of a group of influencers
to estimate how many views a post will get if they all share it.

Complete the summed function. It's a slightly modified version of the algorithm above.
Instead of just two numbers, a and b, it accepts a list of numbers and returns the sum of all of them.
"""

from functools import reduce


def summed(nums: list[int]) -> int:
    return reduce(lambda acc, num: acc + num, nums, 0)


def summed_simple(nums: list[int]) -> int:

    total = 0
    for num in nums:
        total += num
    return total


nums = [1, 3, 5, 6, 8]
print(summed(nums))
print(summed([]))

print(summed_simple(nums))
print(summed_simple([]))
