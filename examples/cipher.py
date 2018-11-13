# -*- coding: utf-8 -*-
from itertools import cycle

def map_key_to_str(key, string):
    return zip(string, cycle(key))


def key_char_to_number(char, abc):
    # number of positions to move based on location of char
    # from key in alphabet
    try:
        return abc.index(char)
    except ValueError:
        return 0

def encode_char(index, abc):
    return abc[index]

class VigenereCipher (object):

    def __init__(self, key, abc):
        self.key = key
        self.abc = abc
        self.code = {char: index for index, char in enumerate(abc)}
        
    def encode(self, text):
        result = ''
        mapping = map_key_to_str(self.key, text)
        for char, key_char in mapping:
            if char not in self.abc:
                result += char
                continue
            pos_to_move = key_char_to_number(key_char, self.abc)
            curr_pos = key_char_to_number(char, self.abc)
            new_pos = (curr_pos + pos_to_move) % len(self.abc)
            new_char = self.abc[new_pos]
            result += new_char

        return result

    def decode(self, text):
        result = ''
        mapping = map_key_to_str(self.key, text)
        for char, key_char in mapping:
            if char not in self.abc:
                result += char
                continue
            pos_to_move = key_char_to_number(key_char, self.abc)
            curr_pos = key_char_to_number(char, self.abc)
            new_pos = (curr_pos - pos_to_move) % len(self.abc)
            new_char = self.abc[new_pos]
            result += new_char
        return result


if __name__ == '__main__':
    print 'Testing now'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = 'password'
    c = VigenereCipher(key, alphabet)

    assert c.encode('codewars') == 'rovwsoiv'
    assert c.encode(u'Привет, засранец') == u'Привет, засранец', c.encode(u'Привет, засранец')
    assert c.decode('laxxhsj') == 'waffles', c.decode('laxxhsj')
    assert c.decode(u'Привет, засранец') == u'Привет, засранец', c.decode(u'Привет, засранец')
