import os

import pytest

import storage

print "Hello from conftest"


@pytest.fixture(scope="session", autouse=True)
def storage_patch():
    print "Hello from fixture"
    original = storage.TEST_DB
    storage.TEST_DB = storage.MemoryDataBase()

    yield None

    print "Bye-bye from fixture"
    storage.TEST_DB = original
