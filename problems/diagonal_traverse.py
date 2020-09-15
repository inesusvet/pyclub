"""
See https://leetcode.com/problems/diagonal-traverse-ii/

Given a list of lists of integers, nums, return all elements of nums in diagonal order as shown in the below images.

"""


def main(nums):
    """
    >>> main([[1,2,3],[4,5,6],[7,8,9]])
    [1, 4, 2, 7, 5, 3, 8, 6, 9]
    >>> main([[1,2,3],[4],[5,6,7],[8],[9,10,11]])
    [1, 4, 2, 5, 3, 8, 6, 9, 7, 10, 11]
    >>> main([[1,2,3,4,5,6]])
    [1, 2, 3, 4, 5, 6]
    >>> main([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]])
    [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16]
    """
