# ~*~ coding: utf-8 ~*~
from __future__ import unicode_literals

import os
import time


def kamikadze():
    print 'Banzai from %d!' % os.getpid()
    exit()


def main():
    pushkin = [
        'Буря моглою, небо кроет,',
        'Вихри снежные крутя;',
        'То, как зверь, она завоет,',
        'То заплачет, как дитя,',
    ]
    print 'We are ready now'

    child_pid = os.fork()
    iam_child = child_pid == 0
    if iam_child:
        parent_pid = os.getppid()
        pid = os.getpid()
        print 'I am new born process %d. My parent is %d' % (pid, parent_pid)
        time.sleep(2)
        print ' I know some poetry!'
        pushkin.extend([
            'То по кровле обветшалой',
            'Вдруг соломой зашумит,',
            'То, как путник запоздалый,',
            'К нам в окошко застучит.',
            '  - A.S.Pushkin, 1825',
        ])
        time
        print '\n'.join(pushkin)
        kamikadze()

    time.sleep(5)
    print '\n'.join('> %s' % line for line in pushkin)
    kamikadze()


if __name__ == '__main__':
    main()

