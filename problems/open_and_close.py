"""
See https://www.codewars.com/kata/all-that-is-open-must-be-closed-dot-dot-dot

## Background
We all know about "balancing parentheses" (plus brackets, braces and chevrons)
and even balancing characters that are identical.

Read that last sentence again, I balanced different characters and identical
characters twice and you didn't even notice... :)

## Kata
Your challenge in this kata is to write a piece of code to validate that a
supplied string is balanced.

You must determine if all that is open is then closed, and nothing is closed
which is not already open!

You will be given a string to validate, and a second string, where each pair
of characters defines an opening and closing sequence that needs balancing.

You may assume that the second string always has an even number of characters.
"""

def is_balanced(text):
    """
    >>> is_balanced('')
    True
    >>> is_balanced('Sensei says yes!')
    True
    >>> is_balanced('(Sensei says yes!)')
    True
    >>> is_balanced('(Sensei says no!')
    False
    >>> is_balanced('(Sensei) (says) (yes!)')
    True
    >>> is_balanced('(Sensei (says) yes!)')
    True
    >>> is_balanced('((Sensei) says) no!)')
    False
    >>> is_balanced('(Sensei (says) (yes!))')
    True
    """
    return False


if __name__ == '__main__':
    import doctest
    failures, errors = doctest.testmod()
