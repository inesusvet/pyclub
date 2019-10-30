"""
Given an array of n integers where each value represents number of chocolates in a packet. Each packet can have variable number of chocolates. There are m students, the task is to distribute chocolate packets such that:
- Each student gets one packet.
- The difference between the number of chocolates in packet with maximum chocolates and packet with minimum chocolates given to the students is minimum.
"""


def optimal_distribution(candy_packets, m):
    """
    >>> optimal_distribution([7, 3, 2, 4, 9, 12, 56], 3)
    2
    >>> optimal_distribution([3, 4, 1, 9, 56, 7, 9, 12], 5)
    6
    >>> optimal_distribution([12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50], 7)
    10
    """
