import pytest
from collections import Counter
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            # actual.append(item.display())
            actual.append(item)

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    actual.reverse()
    # this is not a good fix
    modified_actual = [item if isinstance(item[0], list) else [item] for item in actual]

    assert modified_actual == expected



# @pytest.mark.skip()
def test_key_does_not_exist():
    hashtable = Hashtable()
    actual = hashtable.get("nonexistent")
    expected = None
    assert actual == expected


# @pytest.mark.skip()
def test_unique_keys():
    hashtable = Hashtable(1024)
    hashtable.set("art", 1_000_000)
    hashtable.set("bakery", "cookie")
    hashtable.set("castle", "prince")
    hashtable.set("bakery", "cake")

    keys = hashtable.keys()
    key_counter = {}

    # loop over list of keys and create dictionary
    for key in keys:
        if key not in key_counter:
            key_counter[key] = 1
        else:
            key_counter[key] += 1
    assert all(key_counter.values()) == 1


# test for collision
@pytest.mark.skip()
def test_collision():
    pass


@pytest.mark.skip()
def test_collision_chaining():
    pass


@pytest.mark.skip()
def test_hash_key_in_range():
    pass


