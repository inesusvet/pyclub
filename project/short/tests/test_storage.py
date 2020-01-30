import storage


def test_get__empty_db__none():
    expected = None

    actual = storage.get(0)

    assert actual == expected

