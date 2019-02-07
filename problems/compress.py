
def compress_string(text):
    """
    Write a function which will "compress" input string.
    Instead of repeating a char there should be just number of repetitions.

    >>> compress_string('aaabbbbcddd')
    'a3b4cd3'
    >>> compress_string('abcdefgh')
    'abcdefgh'
    >>> compress_string('aaaaabaaaaa')
    'a5ba5'
    >>> compress_string('aaaaaaaaaab')
    'a10b'
    >>> compress_string('')
    ''
    """
    return


def decompress_string(text):
    """
    Write a inverse function.
    
    >>> decompress_string('')
    ''
    >>> decompress_string('a10b')
    'aaaaaaaaaab'
    >>> decompress_string('a5ba5')
    'aaaaabaaaaa'
    >>> decompress_string('a3b4cd3')
    'aaabbbbcddd'
    """
    return 


if __name__ == '__main__':
    import doctest
    doctest.testmod()
