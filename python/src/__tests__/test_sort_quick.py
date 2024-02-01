import pytest
from src.sort_quick import sort_quick, sort_quick_v2

test_cases = [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([5, 9, 1, 92, 5], [1, 5, 5, 9, 92]),
    ([], []),
    ([1], [1])
]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_sort_quick(test_input, expected):
    assert sort_quick(test_input) == expected


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_sort_quick_v2(test_input, expected):
    assert sort_quick_v2(test_input) == expected
