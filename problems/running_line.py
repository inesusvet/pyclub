# -*- coding: utf-8 -*-

import time

LOREM_IPSUM = """
Lorem ipsum dolor sit amet,
 consectetur adipiscing elit,
 sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
""".replace('\n', '')


def running_line(text, window_size, tick):
    """
    >>> running_line(LOREM_IPSUM, 11, 0)
    '           '
    >>> running_line(LOREM_IPSUM, 11, 5)
    '      Lorem'
    >>> running_line(LOREM_IPSUM, 11, 11)
    'Lorem ipsum'
    >>> running_line(LOREM_IPSUM, 11, 22)
    ' dolor sit '
    >>> running_line(LOREM_IPSUM, 11, 127)
    'aliqua.    '
    >>> running_line(LOREM_IPSUM, 11, 138)
    '       Lore'
    """
    return ''


def demo(text, window_size, sleep_time):
    ticker = 0
    while True:
        line = running_line(text, window_size, ticker)
        print line,
        time.sleep(sleep_time)
        print '\r',
        ticker += 1


if __name__ == '__main__':
    import doctest
    failures, tests = doctest.testmod()

    if failures == 0:
        demo(LOREM_IPSUM, 80, 0.1)
