import random


def mine_coin():
    number = random.random()
    if number >= 0.9:
        raise RuntimeError('Mining failed')
    elif number > 0.95:
        raise Exception('Fatal error')
    return number


def main(n):
    total = i = 0
    while i < n:
        coin = mine_coin()
        total += coin
        i += 1

    return total


if __name__ == '__main__':
    result = main(10)
    print '$', result
