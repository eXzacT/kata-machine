import pytest
from src.graph_to_outtree import graph_to_outtree, tree_to_list_preorder


graph1: dict[str, list[str]] = {
    'A': ['B'],
    'B': ['A', 'G'],
    'C': ['F'],
    'D': ['H'],
    'E': ['F'],
    'F': ['C', 'E', 'G'],
    'G': ['B', 'F', 'I', 'K'],
    'H': ['D', 'K'],
    'I': ['G', 'J'],
    'J': ['I'],
    'K': ['G', 'H']
}

graph2 = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}

test_cases = [
    [[graph1, 'G'], ['G', 'B', 'A', 'F', 'C', 'E', 'I', 'J', 'K', 'H', 'D']],
    [[graph1, 'C'], ['C', 'F', 'E', 'G', 'B', 'A', 'I', 'J', 'K', 'H', 'D']],
    [[graph2, 1], [1, 2, 4, 3]],
    [[graph2, 3], [3, 1, 2, 4]],
]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_convert_to_outtree(test_input, expected):
    graph, root_val = test_input
    assert tree_to_list_preorder(graph_to_outtree(graph, root_val)) == expected
