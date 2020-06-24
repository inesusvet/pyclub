"""
See the original https://leetcode.com/problems/buddy-strings

Given two strings A and B of lowercase letters, return true if and only if we can swap two letters
in A so that the result equals B.
"""


def main(A: str, B: str) -> bool:
    """
    >>> main("ab", "ba")
    True
    >>> main("ab", "ab")
    False
    >>> main("aa", "aa")
    True
    >>> main("aaaaaaabc", "aaaaaaacb")
    True
    >>> main("", "aa")
    False
    """
