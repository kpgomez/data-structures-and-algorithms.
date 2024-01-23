import pytest
from code_challenges.array_reverse import reverse_array


# @pytest.mark.skip
def test_example_one():
    example_one = [1, 2, 3, 4, 5, 6]
    actual = reverse_array(example_one)
    expected = [6, 5, 4, 3, 2, 1]
    assert actual == expected


# @pytest.mark.skip
def test_example_two():
    example_two = [89, 2354, 3546, 23, 10, -923, 823, -12]
    actual = reverse_array(example_two)
    expected = [-12, 823, -923, 10, 23, 3546, 2354, 89]
    assert actual == expected


# @pytest.mark.skip
def test_list_contains_dictionary():
    example_three = [{"1": True},{}]
    actual = reverse_array(example_three)
    expected = [{}, {'1': True}]
    assert actual == expected


# @pytest.mark.skip
def test_list_contains_list():
    list_of_list = ['crazy', []]
    actual = reverse_array(list_of_list)
    expected = [[], 'crazy']
    assert actual == expected


# @pytest.mark.skip
def test_empty_list():
    actual = reverse_array([])
    expected = []
    assert actual == expected


# @pytest.mark.skip
def test_string_input():
    crazy = 'crazy'
    actual = reverse_array(crazy)
    expected = ['y', 'z', 'a', 'r', 'c']
    assert actual == expected

