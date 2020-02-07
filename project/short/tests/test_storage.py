import storage


def test_get__empty_db__none():
    expected = None
    actual = storage.get(0)
    assert actual == expected


def test_get__empty_db_ask_a_number__none():
    expected = None
    actual = storage.get(100500)
    assert actual == expected


def test_get__one_record_in_db__asked_record():
    # arrange
    link_id = storage.put('foobar')

    # act
    actual = storage.get(link_id)

    # assert
    assert actual == 'foobar'


def test_get__one_record_in_db_asked_different_id__none():
    # arrange
    link_id = storage.put('foobar')

    # act
    actual = storage.get(link_id + 1)

    # assert
    assert actual is None
