"""
See https://www.codewars.com/kata/find-all-fridays-the-thirteens/python

Create the function friday13 that accepts a start year and an end year
(inclusive) and returns all of the dates where the 13th of a month lands on
a Friday between the given year(s).

The return value should be a list where each item is an instance of
datetime.date class representing the Friday 13th. Dates expected be in
ascending order.

If end year equals to start year, only return friday the thirteenths during
the start year. If end year is less than start year, empty list should
be returned.

See https://www.youtube.com/watch?v=RjMbCUpvIgw for introduction to datetime module
"""


def friday13(start_year, end_year):
    """
    >>> friday13(1999, 2000)
    [datetime.date(1999, 8, 13), datetime.date(2000, 10, 13)]
    >>> friday13(2014, 2015)
    [datetime.date(2014, 6, 13), datetime.date(2015, 2, 13), datetime.date(2015, 3, 13), datetime.date(2015, 11, 13)]
    >>> friday13(2018, 2018)
    [datetime.date(2018, 4, 13), datetime.date(2018, 7, 13)]
    >>> friday13(2019, 2018)
    []
    """
    return []


if __name__ == '__main__':
    import doctest
    doctest.testmod()
