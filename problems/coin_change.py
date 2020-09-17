def main(coins, amount):
    """
    See https://leetcode.com/problems/coin-change/

    You are given coins of different denominations and a total amount of money. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

    >>> main([], 0)
    0
    >>> main([1], 5)
    5
    >>> main([1, 2], 5)
    3
    >>> main([1, 2, 5], 11)
    3
    >>> main([2], 3)
    -1
    """
