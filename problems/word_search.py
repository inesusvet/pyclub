"""
See https://leetcode.com/problems/word-search/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

[A B C E]
[S F C S]
[A D E E]

"ABCCED" => True
"SEE" => True
"ABCBQ" => False
"""


def main(board, word):
    """
    >>> main([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ABCCED")
    True
    >>> main([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "SEE")
    True
    >>> main([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ABCBQ")
    False
    """
