"""
Assignment
We have a popular influencer using our LockedIn app, and she needs to be able to quickly search for posts from a particular day. This function will be the backbone of her search screen.
Complete the binary_search function. It should follow the algorithm as described above.
"""

"""
Given two inputs:

    A list of n elements sorted from least to greatest
    A target value:

Do the following:

    Set low = 0 and high = n - 1.
    While low <= high:
        Set median (the position of the middle element) to (low + high) // 2, which is the greatest integer less than or equal to (low + high) / 2
        If list[median] == target, return True
        Else if list[median] < target, set low to median + 1
        Otherwise set high to median - 1
    Return False

"""


def binary_search(target: int, arr: list[int]) -> bool:
    low = 0
    high = len(arr) - 1

    while low <= high:
        median = (low + high) // 2

        if arr[median] == target:
            return True
        elif arr[median] < target:
            low = median + 1
        else:
            high = median - 1

    return False


print(binary_search(target=3, arr=[1, 3, 5, 7, 34]))
