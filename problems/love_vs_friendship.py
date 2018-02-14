"""
See https://www.codewars.com/kata/love-vs-friendship/train/python

If　a = 1, b = 2, c = 3 ... z = 26

Then l + o + v + e = 54

and f + r + i + e + n + d + s + h + i + p = 108

So friendship is twice stronger than love :-)

The input will always be in lowercase and never be empty.
"""

def words_to_marks(word):
    return 0


def test():
    assert words_to_marks('attitude') == 100, 'attitude should equal 100'
    assert words_to_marks('friends') == 75, 'friends should equal 75'
    assert words_to_marks('family') == 66, 'family should equal 66'
    assert words_to_marks('selfness') == 99, 'selfness should equal 99'
    assert words_to_marks('knowledge'), 96, 'knowledge should equal 96'


test()
