"""
See the original https://leetcode.com/problems/assign-cookies/

Assume you are an awesome parent and want to give your children some cookies.
But, you should give each child at most one cookie.
Each child i has a greed factor gi, which is the minimum size of a
cookie that the child will be content with; and each cookie j has a size sj.
If sj >= gi, we can assign the cookie j to the child i, and the child i will be content.

Your goal is to maximize the number of your content children and output the maximum number.

Note:
You may assume the greed factor is always positive.
You cannot assign more than one cookie to one child.
"""


def findContentChildren(g, s):
    """
    >>> findContentChildren([1,2,3], [1,1])
    1
    >>> findContentChildren([1,2], [1,2,3])
    2
    >>> findContentChildren(list(range(1, 11)), [1] * 100 + list(range(1, 11)))
    10
    >>> findContentChildren([2, 3, 4, 2], [1, 1, 1, 1])
    0
    >>> findContentChildren([1, 2, 3, 4, 5], [5, 5, 3, 3, 1])
    5
    >>> findContentChildren([1, 2, 3, 4, 5], [])
    0
    """
