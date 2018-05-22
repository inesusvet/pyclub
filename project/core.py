
def encode(number):
    """Converts id number to short text identifier"""
    return str(number)


def decode(slug):
    """Converts short text identifier to a number"""
    return len(slug)


def test():
    """Test that a number doesn't change after being encoded and then decoded"""
    import random

    for random_number in random.sample(range(10 ** 6), 10):
        encoded = encode(random_number)
        decoded = decode(encoded)
        assert random_number == decoded, (random_number, encoded, decoded)


if __name__ == '__main__':
    test()
