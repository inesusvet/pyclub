"""
See original at https://leetcode.com/problems/zigzag-conversion/

The string "DATAROBOTISAWESOME" is written in a zigzag pattern on a given number of rows like this:

D   R   T   W   M
A A O O I A E O E
T   B   S   S

And then read line by line: "DRTWMAAOOIAEOETBSS"

Write the code that will take a string and make this conversion given a number of rows
"""


def convert(text: str, rows: int) -> str:
    """
    >>> convert("DATAROBOTISAWESOME", 3)
    "DRTWMAAOOIAEOETBSS"
    >>> convert("DATAROBOTISAWESOME", 4)
    "DBWAOOAEETRTSSMAIO"
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
