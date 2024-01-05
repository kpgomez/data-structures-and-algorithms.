import pytest
from sorting.merge.merge_sort import merge_sort


@pytest.mark.skip()
def test_sample_array():
    actual = merge_sort.merge_sort([8, 4, 23, 42, 16, 15])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected
