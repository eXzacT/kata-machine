import pytest
from src.sort_selection import sort_selection

test_cases = [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([5, 9, 1, 92, 5], [1, 5, 5, 9, 92]),
    ([], []),
    ([1], [1])
]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_sort_selection(test_input, expected):
    sort_selection(test_input)
    assert test_input == expected
