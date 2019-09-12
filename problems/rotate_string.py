"""
See the original https://leetcode.com/problems/rotate-string/

We are given two strings, A and B.
A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'cdeab', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
"""


def rotate_string(A: str, B: str) -> bool:
    """
    >>> rotate_string('abba', 'aabb')
    True
    >>> rotate_string('', '')
    True
    >>> rotate_string('a' * 100000 + 'b', 'b' + 'a' * 100000)
    True
    >>> rotate_string('a' * 100000 + 'b', 'c' + 'a' * 100000)
    False
    >>> rotate_string('abba', 'baba')
    False
    >>> rotate_string('a', 'aa')
    False
    >>> rotate_string('aa', 'ab')
    False
    """
