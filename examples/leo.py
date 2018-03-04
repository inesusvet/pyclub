#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import logging
import sys
import time

from cipher import VigenereCipher

u"""
Можно скачать Войну и Мир здесь
    http://vojnaimir.ru/files/book1.txt
    http://vojnaimir.ru/files/book2.txt
"""

RUSSIAN = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def timer(func):
    logger = logging.getLogger('timer.%s' % func.__name__)
    def timed(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        finished_at = time.time()
        logger.debug('Function %s run for %.3f sec', func.__name__, finished_at - started_at)
        return result

    return timed


def from_file(filename, **kwargs):
    with codecs.open(filename, 'r', **kwargs) as file_obj:
        for line in file_obj:
            yield line


@timer
def main(abc, key, input, output):
    cipher = VigenereCipher(key.decode('utf'), abc.decode('utf'))
    for line in lines:
        encoded = cipher.encode(line)
        output.write(encoded.encode('utf'))


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print """Use as python leo.py book1.txt cp1251 пароль > my_encoded.txt"""
        exit(1)

    logging.basicConfig(level=logging.DEBUG)
    _, filename, encoding, key = sys.argv

    lines = from_file(filename, encoding=encoding)

    main(RUSSIAN, key, lines, sys.stdout)
    # import cProfile
    # cProfile.run(
    #     'main(RUSSIAN, key, lines, sys.stdout)',
    #     'leostats',
    # )
