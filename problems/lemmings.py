"""
See https://www.codewars.com/kata/lemmings-battle
"""


def is_alive(power):
    """
    Отвечает на вопрос: жив ли лемминг?

    >>> is_alive(0)
    False
    >>> is_alive(100)
    True
    >>> is_alive(-10)
    False
    """


def triage(warriors):
    """
    Отбирает только выживших леммингов после раунда боев.

    >>> triage([10, 0, 5, -2])
    [10, 5]
    """


def fight(green, blue):
    """
    Отвечает на вопрос: сколько силы останется у двух леммингов после их боя?

    >>> fight(10, 10)
    (0, 0)
    >>> fight(12, 10)
    (2, -2)
    >>> fight(10, 15)
    (-5, 5)
    """


def round(green, blue):
    """
    Проводит раунд боев между двумя группами леммингов.
    Количество элементов в каждой группе всегда одинаковое.

    >>> round([1, 2, 3], [3, 2, 1])
    [(-2, 0, 2), (2, 0, -2)]
    >>> round([10], [5])
    [(5,), (-5,)]
    """


def draw(army, size):
    """
    Выбирает из армии нескольких самых сильных леммингов.

    >>> draw([1, 2, 3, 4, 5], 3)
    [5, 4, 3]
    >>> draw([10, 1, 2], 2)
    [10, 2]
    >>> draw([1, 10, 2], 1)
    [10]
    """


def collect(army, warriors):
    """
    Возвращает в армию леммингов, выживших после раунда боев.

    >>> collect([], [1, 2, 3])
    [1, 2, 3]
    >>> collect([10, 9, 8, 7], [1, 2, 3])
    [10, 9, 8, 7, 1, 2, 3]
    """


def lemming_battle(battlefield, green, blue):
    """
    Проводит войну между двумя армиями леммингов на заданном количестве полей.
    """


def test():
    assert lemming_battle(5, [10], [10]) == "Green and Blue died"
    assert lemming_battle(2, [20,10], [10,10,15]) == "Blue wins: 5"
    assert lemming_battle(3, [50,40,30,40,50], [50,30,30,20,60]) == "Green wins: 10 10"


if __name__ == '__main__':
    test()
