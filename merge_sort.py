"""
Algorithm

The algorithm consists of two separate functions, merge_sort() and merge().

merge_sort() divides the input array into two halves, calls itself on each half, and then merges the two sorted halves back together in order.

The merge() function merges two already sorted lists back into a single sorted list. At the lowest level of recursion, the two "sorted" lists will each only have one element. Those single element lists will be merged into a sorted list of length two, and we can build from there.

In other words, all the "real" sorting happens in the merge() function.
merge_sort() pseudocode

Input: A, an unsorted list of integers

    If the length of A is less than 2, it's already sorted so return it
    Split the input array into two halves down the middle
    Call merge_sort() twice, once on each half
    Return the result of calling merge(sorted_left_side, sorted_right_side) on the results of the merge_sort() calls

merge() pseudocode

Inputs: A and B. Two sorted lists of integers

    Create a new final list of integers.
    Set i and j equal to zero. They will be used to keep track of indexes in the input lists (A and B).
    Use a loop to compare the current elements of A and B:
        While i < len(A) and j < len(B), compare A[i] and B[j].
        Append the smaller or equal value to final.
        Increment the index for the list you just took from.
        Stop when either list is exhausted.
    After comparing all the items, there may be some items left over in either A or B. Add those extra items to the final list.
    Return the final list.

"""


def merge_sort(nums: list[int]) -> list[int]:
    pass


def merge(first: list[int], second: list[int]) -> list[int]:
    pass
