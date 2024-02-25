import pytest
from src.binary_trees import *

test_cases = [
    ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
    ([2, 1, 3], [2, 3, 1]),
    ([], []),
]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_invert_tree(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in [invert_tree_iter, invert_tree_rec]:
        head = create(test_input)
        assert display(func(head)) == expected


test_cases = [
    ([3, 9, 20, None, None, 15, 7], 3),
    ([1, None, 2], 2),
    ([], 0),
    ([0], 1),
]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_max_depth(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in [max_depth_iter, max_depth_dfs, max_depth_dfs_v2, max_depth_bfs]:
        assert func(create(test_input)) == expected


test_cases = [
    ([1, 2, 3, 4, 5], 3),
    ([1, 2], 1),
    ([], 0),
]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_max_diameter(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in [max_diameter_dfs, max_diameter_dfs_v2]:
        assert func(create(test_input)) == expected


test_cases = [
    ([3, 9, 20, None, None, 15, 7], True),
    ([1, 2, 2, 3, 3, None, None, 4, 4], False),
    ([], True),
]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_is_balanced(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in [is_balanced_dfs, is_balanced_dfs_v2]:
        assert func(create(test_input)) == expected


test_cases = [
    (([1, 2, 3], [1, 2, 3]), True),
    (([1, 2], [1, None, 2]), False),
    (([1, 2, 1], [1, 1, 2]), False),
    (([], []), True),
]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_is_same(test_input, expected):
    print(f"\nFor input {test_input}")
    l1, l2 = test_input
    tree1, tree2 = create(l1), create(l2)

    for func in [is_same_dfs, is_same_iter, is_same_bfs]:
        assert func(tree1, tree2) == expected
