import string

ABC = string.ascii_letters + string.digits + '-_+='

def encode(number):
    """Converts id number to short text identifier.

    >>> encode(1)
    'b'
    >>> encode(10000)
    'ctI'
    >>> encode(66)
    'ba'
    """
    result = []
    rest = number
    abc_len = len(ABC)

    while rest >= abc_len:
        result.append(ABC[rest % abc_len])
        rest = rest // abc_len

    result.append(ABC[rest])

    return ''.join(result[::-1])


def decode(slug):
    """Converts short text identifier to a number.

    >>> decode('b')
    1
    >>> decode('ctI')
    10000
    >>> decode('ba')
    66
    """
    result = []
    abc_len = len(ABC)

    for symbol in slug:
        result.append(ABC.index(symbol))

    number = 0
    for i, n in enumerate(result[::-1]):
        number += n * (abc_len ** i)

    return number


def test_random_encoding_and_decoding(verbose=False):
    """Test that a number doesn't change after being encoded and then decoded"""
    import random

    for random_number in random.sample(range(10 ** 6), 10):
        if verbose:
            print "Going to test encoding/decoding with %s" % random_number,

        encoded = encode(random_number)
        decoded = decode(encoded)

        if verbose:
            print ": Encoded to %r; Decoded to %r" % (encoded, decoded),

        assert random_number == decoded, "%s >> %s >> %s" % (random_number, encoded, decoded)

        if verbose:
            print "= OK"


if __name__ == '__main__':
    import sys

    print "Testing stuff"

    use_verbose = '-v' in sys.argv
    test_random_encoding_and_decoding(verbose=use_verbose)
