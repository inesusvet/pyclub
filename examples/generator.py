"""
Build a generator function which will
 _find_ all `*.log` files in the current directory,
 _sort_ file names by file's creation time, and will
 _print out_ lines from every file to stdout.
"""

import os


def find(root, mask):
    """
    Yields filenames from `root` matching specified `mask`
    ordered by increasing the file's creation time
    """
    yield  # TODO: Implement this


def lines_from_file(filename):
    """Yeilds all lines from a secified file"""
    with open(filename) as file_obj:
        for line in file_obj:
            yield line


def main(root, mask):
    for filename in generate_filenames_by_creation_time(root, mask):
        for line in lines_from_file(filename):
            print line


if __name__ == '__main__':
    root = os.path.getcwd()
    mask = '*.log'

    main(root, mask)
