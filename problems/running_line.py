# -*- coding: utf-8 -*-

import time

LOREM_IPSUM = """
Lorem ipsum dolor sit amet,
 consectetur adipiscing elit,
 sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
""".replace('\n', '')


def running_line(text, window_size, tick):
    """
    >>> running_line(LOREM_IPSUM, 10, 0)
    '          '
    >>> running_line(LOREM_IPSUM, 10, 1)
    '         L'
    >>> running_line(LOREM_IPSUM, 11, 11)
    'Lorem ipsum'
    """
    return ''


def demo(text, window_size, sleep_time):
    ticker = 0
    while True:
        line = running_line(text, window_size, ticker).encode('utf-8')
        print line,
        time.sleep(sleep_time)
        print '\r',
        ticker += 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # demo(LOREM_IPSUM, 80, 0.1)
