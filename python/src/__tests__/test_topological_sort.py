import pytest
from src.topological_sort import topological_sort_dfs, topological_sort_dfs_v2, topological_sort_bfs
from common import time_execution

dag: dict[int, list[int]] = {
    0: [3, 6],
    1: [3],
    2: [4, 5],
    3: [6, 7],
    4: [3, 7, 8],
    5: [4, 8],
    6: [7, 9],
    7: [10],
    8: [11],
    9: [10, 12],
    10: [12, 14],
    11: [14],
    12: [],
    13: [14],
    14: []
}

cyclic: dict[int, list[int]] = {
    0: [3, 6],
    1: [3],
    2: [4, 5],
    3: [6, 7],
    4: [3, 8],
    5: [4, 8],
    6: [7, 9],
    7: [4, 10],
    8: [11],
    9: [10, 12],
    10: [12, 14],
    11: [14],
    12: [],
    13: [14],
    14: []
}

test_cases = [
    (dag, [13, 2, 5, 4, 8, 11, 1, 0, 3, 6, 9, 7, 10, 14, 12]),
    (cyclic, []),
]


@time_execution
@pytest.mark.parametrize("test_input,expected", test_cases)
def test_topological_sort_dfs(test_input, expected):
    assert topological_sort_dfs(test_input) == expected


@time_execution
@pytest.mark.parametrize("test_input,expected", test_cases)
def test_topological_sort_dfs_v2(test_input, expected):
    assert topological_sort_dfs_v2(test_input) == expected


@time_execution
@pytest.mark.parametrize("test_input,expected", test_cases)
def test_topological_sort_bfs(test_input, expected):
    assert topological_sort_bfs(test_input) == expected
