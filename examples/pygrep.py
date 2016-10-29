#!/usr/bin/env python

import subprocess
import sys


def grep(pattern, filenames):
    return subprocess.check_output(['grep', pattern] + filenames)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "Need pattern to search and filenames"
        exit(1)

    print grep(sys.argv[1], sys.argv[2:])
