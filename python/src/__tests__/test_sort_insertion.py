import pytest
from src.sort_insertion import sort_insertion
from common import time_execution

test_cases = [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([5, 9, 1, 92, 5], [1, 5, 5, 9, 92]),
    ([], []),
    ([1], [1])
]


@pytest.mark.parametrize("test_input,expected", test_cases)
@time_execution
def test_sort_insertion(test_input, expected):
    sort_insertion(test_input)
    assert test_input == expected
