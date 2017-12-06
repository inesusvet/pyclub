import threading
import time

import requests


def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print time.time() - start
        return result
    return inner


def _thread_target(link):
    return requests.get(link)


@timer
def main_threading(*links):
    threads = []
    for link in links:
        thread = threading.Thread(target=_thread_target, args=(link, ))
        thread.start()
        threads.append(thread)

    for th in threads:
        th.join()


@timer
def main_gevent(*links):
    from gevent import monkey
    monkey.patch_all()

    for link in links:
        resp = requests.get(link)


@timer
def main(*links):
    for link in links:
        requests.get(link)


if __name__ == '__main__':
    links = ('http://vojnaimir.ru/files/book1.txt', 'http://vojnaimir.ru/files/book2.txt')

    print 'Serial',
    main(*links)

    print 'Threads',
    main_threading(*links)

    print 'Gevent',
    main_gevent(*links)

