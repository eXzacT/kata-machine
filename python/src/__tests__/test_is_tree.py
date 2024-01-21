import pytest
from src.is_tree import is_tree
from common import time_execution

graph1 = {'A': ['B'],
          'B': ['A', 'G'],
          'C': ['F'],
          'D': ['H'],
          'E': ['F'],
          'F': ['C', 'E', 'G'],
          'G': ['B', 'F', 'I', 'K'],
          'H': ['D', 'K'],
          'I': ['G', 'J'],
          'J': ['I'],
          'K': ['G', 'H']}

graph2 = {'A': ['B'],
          'B': ['A', 'G'],
          'C': ['F'],
          'D': ['H'],
          'E': ['F'],
          'F': ['C', 'E', 'G'],
          'G': ['B', 'F', 'I'],
          'H': ['D', 'K'],
          'I': ['G', 'J'],
          'J': ['I'],
          'K': ['H']}

graph3 = {'A': ['B'],
          'B': ['A', 'G'],
          'C': ['F', 'E'],
          'D': ['H'],
          'E': ['F', 'C'],
          'F': ['C', 'E', 'G'],
          'G': ['B', 'F', 'I', 'K'],
          'H': ['D', 'K'],
          'I': ['G', 'J'],
          'J': ['I'],
          'K': ['G', 'H']}

# Acyclic,undirected,connected,edges-1=verts->Tree
graph4 = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}

# Cycle
graph5 = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2]
}

# Disconnected
graph6 = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2],
    5: [6],
    6: [5, 7],
    7: [6]
}


test_cases = [
    [graph1, True],
    [graph2, False],
    [graph3, False],
    [graph4, True],
    [graph5, False],
    [graph6, False],
]


@time_execution
@pytest.mark.parametrize("test_input,expected", test_cases)
def test_is_tree(test_input, expected):
    assert is_tree(test_input) == expected
