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
    print(hashtable.has("apple"))
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

    reformatted_expected = []

    for item in expected:
        if len(item) > 1:
            for sub_item in item:
                reformatted_expected.append(sub_item)
        if len(item) == 1:
            reformatted_expected.append(item)

    count = 0

    for expected_item in reformatted_expected:
        if expected_item in actual:
            count += 1

    for expected_item in reformatted_expected:
        for sub_item in expected_item:
            if sub_item in actual:
                count += 1

    assert count == len(actual)


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
    counter = Counter(hashtable.keys())
    assert(all(counter.values()) == 1)

