# -*- coding: utf-8 -*-

def reverse_words(text):
    """
    >>> reverse_words("Let's take LeetCode contest")
    "s'teL ekat edoCteeL tsetnoc"
    >>> reverse_words("")
    ''
    >>> reverse_words(" ")
    ' '
    >>> reverse_words("foo")
    'oof'
    >>> reverse_words(" bar ")
    ' rab '
    >>> reverse_words("foo  bar")
    'oof  rab'
    >>> reverse_words("foo.bar")
    'rab.oof'
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
