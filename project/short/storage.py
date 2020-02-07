import json
import shelve

DATABASE = 'links'  # {'number': 'link'}
INDEX = 'index'  # {'link hash': number}
TEST_DB = None  # Bad practice


class DataBase(object):
    def open(self, filename):
        self.db = shelve.open(filename)

    def close(self):
        self.db.close()

    def keys(self):
        return self.db.keys()

    def get(self, name):
        return self.db.get(name)

    def put(self, name, value):
        self.db[name] = value


class MemoryDataBase(dict):
    def open(self, filename):
        self.opened = True
    def close(self):
        self.opened = False

    def put(self, key, value):
        self[key] = value


class JSONDataBase(object):
    def open(self, filename):
        self._filename = filename + ".json"
        with open(filename) as fo:
            self.db = json.load(fo)

    def close(self):
        with open(self._filename, 'w') as fo:
            json.dump(self.db, fo)

    def keys(self):
        return self.db.keys()

    def get(self, name):
        return self.db.get(name)

    def put(self, name, value):
        self.db[name] = value


def get_database():
    if TEST_DB is not None:
        return TEST_DB
    return DataBase()


def find(link):
    """Returns an id if this link already was saved or None if not"""
    db = get_database()
    db.open(INDEX)
    link_hash = hash(link)
    number = db.get(str(link_hash))
    db.close()
    return number


def get(number):
    """Takes id of the link and returns original link as text"""
    db = get_database()
    db.open(DATABASE)
    value = db.get(str(number))
    db.close()
    return value


def put(link):
    """Saves link to storage and returns id assigned"""
    db = get_database()
    db.open(DATABASE)
    all_keys = db.keys()
    all_numbers = [int(k) for k in all_keys] if len(all_keys) else [-1]
    number = max(all_numbers)
    key = number + 1

    db.put(str(key), link)
    db.close()
    print db

    index = get_database()
    index.open(INDEX)
    link_hash = hash(link)
    index.put(str(link_hash), key)
    index.close()

    return key
