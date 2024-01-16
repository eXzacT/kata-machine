import pytest
from src.sort_shell import sort_shell
from common import time_execution

test_cases = [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([9, 6, 21, 3, 2, 25, 1], [1, 2, 3, 6, 9, 21, 25]),
    ([], []),
    ([1], [1])
]


@time_execution
@pytest.mark.parametrize("test_input,expected", test_cases)
def test_sort_shell(test_input, expected):
    sort_shell(test_input)
    assert test_input == expected
