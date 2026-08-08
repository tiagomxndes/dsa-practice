"""
Assignment
While our avocado toast influencers were happy with our search functionality, now they want to be able to sort all their followers by follower count.
Bubble sort is a straightforward sorting algorithm that we can implement quickly, so let's do that!
Complete the bubble_sort function according to the described algorithm above.
"""

"""
Set swapping to True
Set end to the length of the input list
While swapping is True:

    Set swapping to False
    For i from the 2nd element to end:
        If the (i-1)th element of the input list is greater than the ith element:
            Swap the (i-1)th element and the ith element
            Set swapping to True
    Decrement end by one

Return the sorted list
"""


def bubble_sort(nums: list[int]) -> list[int]:

    swapping = True
    end = len(nums)

    while swapping:
        swapping = False

        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True
        end -= 1

    return nums


def bubble(nums):

    sorted = False
    ending_list = len(nums)

    while not sorted:
        sorted = True

        for i in range(0, ending_list - 1):
            if nums[i] > nums[i + 1]:
                sorted = False
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums


print(bubble_sort([1, 5, 8, 4, 3, 7]))
print(bubble([3, 6, 8, 12, 2, 77]))
