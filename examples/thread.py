import time
import threading
import signal

is_enabled = True


def sig_int(sig, stack):
    print 'sigint!'
    is_enabled = False

signal.signal(signal.SIGINT, sig_int)


def spam(name, sleep):
    while is_enabled:
        print name, is_enabled
        time.sleep(sleep)


th2 = threading.Thread(target=spam, args=('Controlled thread', 2), name='Thread')
th2.start()

while True:
    time.sleep(1)

