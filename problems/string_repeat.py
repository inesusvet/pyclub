"""
See http://www.codewars.com/kata/string-repeat

Write a function called repeatStr which repeats the given string string exactly n times.
"""

def repeatStr(number, text):
    """
    >>> repeatStr(6, 'I')
    'IIIIII'
    >>> repeatStr(5, 'Hello')
    'HelloHelloHelloHelloHello'
    """
    return ''


if __name__ == '__main__':
    import doctest
    failures, errors = doctest.testmod()
