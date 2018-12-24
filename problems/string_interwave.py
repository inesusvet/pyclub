"""
See https://www.codewars.com/kata/interweaving-strings-and-removing-digits
"""


def remove_digits(text):
    """
    >>> remove_digits('1234512')
    ''
    >>> remove_digits('abc123def')
    'abcdef'
    >>> remove_digits('1a2bc3d4ef5')
    'abcdef'
    """
    return ''


def collapse(left, right):
    """
    >>> collapse('', '')
    ''
    >>> collapse('a', 'b')
    'ab'
    >>> collapse('1234', 'abcd')
    '1a2b3c4d'
    >>> collapse('12', 'a')
    '1a2'
    """
    return ''


def interweave(m1, m2):
    """
    >>> interweave('hlo', 'el')
    'hello'
    >>> interweave('h3lo', 'el4')
    'hello'
    """
    return ''
