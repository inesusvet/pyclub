import shelve

DATABASE = 'links'  # {'number': 'link'}
INDEX = 'index'  # {'link hash': number}


def find(link):
    """Returns an id if this link already was saved or None if not"""
    db = shelve.open(INDEX)
    link_hash = hash(link)
    number = db.get(str(link_hash))
    db.close()
    return number


def get(number):
    """Takes id of the link and returns original link as text"""
    db = shelve.open(DATABASE)
    value = db.get(str(number))
    db.close()
    return value


def put(link):
    """Saves link to storage and returns id assigned"""
    db = shelve.open(DATABASE)
    all_keys = db.keys()
    all_numbers = [int(k) for k in all_keys] if len(all_keys) else [-1]
    number = max(all_numbers)
    key = number + 1

    db[str(key)] = link
    db.close()

    db = shelve.open(INDEX)
    link_hash = hash(link)
    db[str(link_hash)] = key
    db.close()

    return key
