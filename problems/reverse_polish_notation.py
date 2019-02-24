"""
See https://www.codewars.com/kata/reverse-polish-notation-calculator

Your job is to create a calculator which evaluates expressions in Reverse Polish notation.
For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.
For your convenience, the input is formatted such that a space is provided between every token.
Empty expression should evaluate to 0.
Valid operations are +, -, *, /.
You may assume that there won't be exceptional situations (like stack underflow or division by zero).
"""


def calc(expr):
    """
    >>> calc("")
    0
    >>> calc("3")
    3
    >>> calc("3.5")
    3.5
    >>> calc("1 3 +")
    4
    >>> calc("1 3 *")
    3
    >>> calc("1 3 -")
    -2
    >>> calc("4 2 /")
    2
    >>> calc("5 1 2 + 4 * + 3 -")
    14
    """
    return 0
