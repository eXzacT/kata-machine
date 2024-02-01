import pytest
from src.distance_k_tree import distance_k_tree_bfs, distance_k_tree_dfs

adjancency_list: dict[str, list[str]] = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H', 'I', 'J'],
    'E': ['K'],
    'F': ['L', 'M'],
    'G': [],
    'H': ['N'],
    'I': [],
    'J': ['O'],
    'K': [],
    'L': ['P', 'Q'],
    'M': ['R'],
    'N': [],
    'O': ['S', 'T'],
    'P': [],
    'Q': [],
    'R': [],
    'S': [],
    'T': []
}

test_cases = [
    ((adjancency_list, 'B', 3), set(['P', 'Q', 'R', 'G', 'H', 'I', 'J'])),
    ((adjancency_list, 'G', 3), set(['B', 'D']))
]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_distance_k_tree_bfs(test_input, expected):
    assert distance_k_tree_bfs(*test_input) == expected


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_distance_k_tree_dfs(test_input, expected):
    assert distance_k_tree_dfs(*test_input) == expected
