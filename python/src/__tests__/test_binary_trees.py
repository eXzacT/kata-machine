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


test_cases = [
    (([3, 4, 5, 1, 2], [4, 1, 2]), True),
    (([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2]), False),
    (([1, 1], [1]), True),
    (([3, 4, 5, 1, None, 2], [3, 1, 2]), False),
    (([4, 1, None, 1, None, 6, 7], [4, 1, None, 6, 7]), False),
    (([1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1,
     None, 1, None, 1, 2], [1, None, 1, None, 1, None, 1, None, 1, None, 1, 2]), True),
]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_is_subtree(test_input, expected):
    print(f"\nFor input {test_input}")
    l1, l2 = test_input
    tree1, tree2 = create(l1), create(l2)

    for func in [is_subtree, is_subtree_v2]:
        assert func(tree1, tree2) == expected


test_cases = [
    (([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8), 6),
    (([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4), 2),
    (([2, 1], 2, 1), 2),
    (([28, 12, 45, 4, 24, 35, 47, 2, 9, 14, 25, 31, 42, 46, 48, 0, 3, 8, 11, 13, 20, None, 26, 30, 33, 41, 43, None, None, None, 49, None, 1, None, None, 7, None, 10, None, None, None, 17, 22, None, 27, 29, None, 32, 34, 36, None, None, 44, None, None,
     None, None, 6, None, None, None, 16, 18, 21, 23, None, None, None, None, None, None, None, None, None, 37, None, None, 5, None, 15, None, None, 19, None, None, None, None, None, 40, None, None, None, None, None, None, 39, None, 38], 1, 23), 12),
]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_lowest_common_ancestor(test_input, expected):
    print(f"\nFor input {test_input}")
    l, p, q = test_input
    tree = create(l)
    p, q = TreeNode(p), TreeNode(q)

    for func in [lowest_common_ancestor, lowest_common_ancestor_v2, lowest_common_ancestor_v3]:
        assert func(tree, p, q).val == expected


test_cases = [
    ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
    ([1], [[1]]),
    ([], []),
]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_lowest_common_ancestor(test_input, expected):
    print(f"\nFor input {test_input}")

    for func in [level_order_traversal_iter, level_order_traversal_rec]:
        assert func(create(test_input)) == expected
