from itertools import cycle, islice


class Dict(dict):
    def __missing__(self, key):
        return key


class VigenereCipher (object):
    def __init__(self, key, alphabet):
        self.key = key
        alphabet = alphabet
        self.cipher = {
            letter: Dict({
                letter: encoded
                for letter, encoded in zip(alphabet, islice(cycle(alphabet), i, i + len(alphabet)))
            })
            for i, letter in enumerate(alphabet)
        }
        
    def encode(self, str):
        return ''.join(self.cipher[key][letter] for letter, key in zip(str, cycle(self.key)))

    def decode(self, str):
        codebook = Dict({key: {v: k for k, v in book.iteritems()} for key, book in self.cipher.iteritems()})
        return ''.join(codebook[key][letter] for letter, key in zip(str, cycle(self.key)))

