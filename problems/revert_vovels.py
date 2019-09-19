"""
See the original https://leetcode.com/problems/reverse-vowels-of-a-string/

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"

Note:
The vowels does not include the letter "y".
"""


def revert_vovels(text):
    """
    >>> revert_vovels("hello")
    'holle'
    >>> revert_vovels("leetcode")
    'leotcede'
    >>> revert_vovels("")
    ''
    >>> revert_vovels('bc"d')
    'bc"d'
    >>> revert_vovels("AcdO")
    'OcdA'
    >>> revert_vovels("bad")
    'bad'
    """
