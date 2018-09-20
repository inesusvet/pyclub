"""
See https://www.codewars.com/kata/lemmings-battle
"""


def is_alive(power):
    """
    >>> is_alive(0)
    False
    >>> is_alive(100)
    True
    >>> is_alive(-10)
    False
    """


def triage(warriors):
    """
    >>> triage([10, 0, 5, -2])
    [10, 5]
    """


def fight(green, blue):
    """
    >>> fight(10, 10)
    (0, 0)
    >>> fight(12, 10)
    (2, -2)
    >>> fight(10, 15)
    (-5, 5)
    """


def round(green, blue):
    """
    >>> round([1, 2, 3], [3, 2, 1])
    [(-2, 0, 2), (2, 0, -2)]
    >>> round([10], [5])
    [(5,), (-5,)]
    """


def draw(army, size):
    """
    >>> draw([1, 2, 3, 4, 5], 3)
    [5, 4, 3]
    >>> draw([10, 1, 2], 2)
    [10, 2]
    >>> draw([1, 10, 2], 1)
    [10]
    """


def collect(army, warriors):
    """
    >>> collect([], [1, 2, 3])
    [1, 2, 3]
    >>> collect([10, 9, 8, 7], [1, 2, 3])
    [10, 9, 8, 7, 1, 2, 3]
    """


def lemming_battle(battlefield, green, blue):
    pass


def test():
    assert lemming_battle(5, [10], [10]) == "Green and Blue died"
    assert lemming_battle(2, [20,10], [10,10,15]) == "Blue wins: 5"
    assert lemming_battle(3, [50,40,30,40,50], [50,30,30,20,60]) == "Green wins: 10 10"


if __name__ == '__main__':
    test()
