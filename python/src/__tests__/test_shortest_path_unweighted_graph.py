import pytest
from src.shortest_path_unweighted_graph import *


graph: dict[str, list[str]] = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'I'],
    'C': ['A', 'B', 'F'],
    'D': ['A', 'G'],
    'E': ['C', 'H'],
    'F': ['C', 'H', 'J'],
    'G': ['C', 'D', 'I'],
    'H': ['C', 'E', 'F', 'I'],
    'I': ['B', 'G', 'K'],
    'J': ['F', 'K'],
    'K': ['I', 'J']
}

test_cases = [
    [(graph, 'A', 'I'), ['A', 'B', 'I']],
    [(graph, 'A', 'K'), ['A', 'B', 'I', 'K']],
]

functions = [globals()[name] for name in dir() if 'shortest' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_filename(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
