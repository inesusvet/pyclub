import os

import pytest

import storage

print "Hello from conftest"


@pytest.fixture(scope="session", autouse=True)
def storage_patch():
    print "Hello from fixture"
    original = storage.DATABASE
    storage.DATABASE = 'test'

    yield None

    print "Bye-bye from fixture"
    storage.DATABASE = original
    os.remove('test.db')
