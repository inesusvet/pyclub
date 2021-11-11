from collections import Counter
import operator

right = {'m': 4, 'q': 3, 'd': 2, 'z': 1, 'y': 3}
left = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'y': 1}
center = {letter: 1 for letter in "aeuioy"}


def fight(text):
    letters = Counter(text)
    counters = {'right': 0,
                'left': 0,
                'center': 0}
    for key, value in letters.items():
        if key in right:
            counters['right'] += value * right[key]
        if key in left:
            counters['left'] += value * left[key]
        if key in center:
            counters['center'] += value
    # sorted_dict = sorted(counters.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = sorted(counters.items(), key=operator.itemgetter(1), reverse=True)
    if sorted_dict[0][1] != sorted_dict[1][1]:
        return '{} side wins!'.format(sorted_dict[0][0].capitalize())
    else:
        return "Let's fight again!"


print(fight('abracadabra'))

