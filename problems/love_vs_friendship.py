"""
See https://www.codewars.com/kata/love-vs-friendship/train/python

If　a = 1, b = 2, c = 3 ... z = 26

Then l + o + v + e = 54

and f + r + i + e + n + d + s + h + i + p = 108

So friendship is twice stronger than love :-)

The input will always be in lowercase and never be empty.
"""

def words_to_marks(word):
    """
    >>> words_to_marks('attitude')
    100
    >>> words_to_marks('friends')
    75
    >>> words_to_marks('family')
    66
    >>> words_to_marks('selfness')
    99
    >>> words_to_marks('knowledge')
    96
    """
    return 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
