"""
See http://www.codewars.com/kata/palindrome-strings

A palindrome is a word, phrase, number, or other sequence of characters which
reads the same backward or forward. This includes capital letters, punctuation,
and word dividers.
"""

def is_palindrome(string):
    """
    >>> is_palindrome('anna')
    True
    >>> is_palindrome('Walter')
    False
    >>> is_palindrome(12321)
    True
    >>> is_palindrome(123456)
    False
    """
    return


def is_palindrome_ingoring_case_and_non_letter_chars(text):
    """
    >>> is_palindrome("anna")
    True
    >>> is_palindrome("madam")
    True
    >>> is_palindrome("foobar")
    False
    >>> is_palindrome("anna:)")
    True
    >>> is_palindrome("Anna")
    True
    >>> is_palindrome("Race car!")
    True
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()
