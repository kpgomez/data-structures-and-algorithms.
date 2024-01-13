import pytest
from code_challenges.hashtable_left_join import left_join


def test_exists():
    assert left_join


# @pytest.mark.skip("TODO")
def test_example():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = [
        ["fond", "enamored", "averse"],
        ["wrath", "anger", "delight"],
        ["diligent", "employed", "idle"],
        ["outfit", "garb", "NONE"],
        ["guide", "usher", "follow"],
    ]

    actual = left_join(synonyms, antonyms)

    assert sorted(actual) == sorted(expected)  # added sorted method


# @pytest.mark.skip()
def test_words_and_other_words():
    words = {
        "nice": "cordial",
        "happy": "joyful",
        "beneath": "under",
        "smart": "bright",
        "hot": "warm",
    }
    other_words = {
        "nice": "mean",
        "happy": "sad",
        "over": "below",
        "smart": "dull",
        "hot": "cold",
    }

    expected = [
        ["nice", "cordial", "mean"],
        ["happy", "joyful", "sad"],
        ["beneath", "under", "NONE"],
        ["smart", "bright", "dull"],
        ["hot", "warm", "cold"],
    ]

    actual = left_join(words, other_words)

    assert sorted(actual) == sorted(expected)


# @pytest.mark.skip()
def test_abcd():
    abc = {
        "A": "another",
        "B": "both",
        "C": "covered"
    }

    acd = {
        "A": "apple",
        "C": "classic",
        "D": "down"
    }

    expected = [
        ["A", "another", "apple"],
        ["B", "both", "NONE"],
        ["C", "covered", "classic"]
    ]

    actual = left_join(abc, acd)

    assert sorted(actual) == sorted(expected)


# @pytest.mark.skip()
def test_two_empty_dictionaries():
    actual = left_join({},{})
    expected = None
    assert actual == expected


# @pytest.mark.skip()
def test_left_dictionary_empty():
    other_words = {
        "D": "drifting",
        "E": "elephant",
        "F": "father"
    }
    actual = left_join({}, other_words)
    expected = None

    assert actual == expected


# @pytest.mark.skip()
def test_right_dictionary_empty():
    other_words = {
        "D": "drifting",
        "E": "elephant",
        "F": "father"
    }
    actual = left_join(other_words, {})
    expected = None

    assert actual == expected
