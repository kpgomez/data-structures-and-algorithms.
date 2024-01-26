import pytest
from code_challenges.sum_rows import sum_rows


# @pytest.mark.skip()
def test_example_one():
    example_one = [[1, 2, 3], [3, 5, 7], [1, 7, 10]]
    actual = sum_rows(example_one)
    expected = [6, 15, 18]
    assert actual == expected


# @pytest.mark.skip()
def test_example_two():
    example_two = [[0, 1, 5], [-4, 7, 2], [-3, 12, 11]]
    actual = sum_rows(example_two)
    expected = [6, 5, 20]
    assert actual == expected


# @pytest.mark.skip()
def test_example_three():
    example_three = [[1, 4, 9,], [0, 7], [1], []]
    actual = sum_rows(example_three)
    expected = [14, 7, 1, 0]
    assert actual == expected


# @pytest.mark.skip()
def test_edge_example():
    edge_example = [["abc"], [8, 7], [1, 9, 8]]
    actual = sum_rows(edge_example)
    expected = [0, 15, 18]


# @pytest.mark.skip()
def test_empty_example():
    empty_example = [[],[],[]]
    actual = sum_rows(empty_example)
    expected = [0, 0, 0]
    assert actual == expected
