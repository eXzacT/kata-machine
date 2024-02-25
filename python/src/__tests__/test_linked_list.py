import pytest
from src.linked_list import *


def test_linked_list():
    ll = LinkedList(ListNode(1))

    assert ll.display() == [1]
    ll.reverse()
    assert ll.display() == [1]
    ll.reverse_rec()
    assert ll.display() == [1]

    ll.head.nxt = ListNode(2)
    ll.reverse()
    assert ll.display() == [2, 1]
    ll.reverse_rec()
    assert ll.display() == [1, 2]

    ll.head.nxt.nxt = ListNode(3)
    ll.head.nxt.nxt.nxt = ListNode(4)
    ll.head.nxt.nxt.nxt.nxt = ListNode(5)

    ll.reverse()
    assert ll.display() == [5, 4, 3, 2, 1]
    ll.reverse_rec()
    assert ll.display() == [1, 2, 3, 4, 5]


test_cases = [
    (([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]),
    (([1, 2, 4, 10, 15, 17], [1, 3, 4, 7, 9, 10, 11]),
     [1, 1, 2, 3, 4, 4, 7, 9, 10, 10, 11, 15, 17]),
    (([], []), []),
    (([], [0]), [0]),
]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_merge_two_sorted_linked_lists(test_input, expected):
    l1, l2 = test_input
    h1, h2 = init_ll(l1), init_ll(l2)
    # Display as a list when given a head reference
    assert display(merge_two_sorted_lls(h1, h2)) == expected


test_cases = [
    (([2, 4, 3], [5, 6, 4]), [7, 0, 8]),
    (([0], [0]), [0]),
    (([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]), [8, 9, 9, 9, 0, 0, 0, 1]),
    (([5, 2, 1, 3, 4], [4, 1, 1, 3, 4, 3, 2]), [9, 3, 2, 6, 8, 3, 2]),
    (([3, 7], [9, 2]), [2, 0, 1]),
]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_add_two_lists(test_input, expected):
    l1, l2 = test_input
    h1, h2 = init_ll(l1), init_ll(l2)
    # Display as a list when given a head reference
    assert display(sum_two_linked_lists(h1, h2)) == expected


test_cases = [
    (([1, 2, 3, 4, 5], 2), [1, 2, 3, 5]),
    (([1], 1), []),
    (([1, 2], 1), [1]),
    (([5, 2, 1, 3, 4], 3), [5, 2, 3, 4]),
    (([1, 2], 2), [2]),
]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_remove_nth_from_the_back(test_input, expected):
    print(f"\nFor input {test_input}")
    l, k = test_input
    # Display as a list when given a head reference
    for func in [remove_nth_from_end_naive, remove_nth_from_end_optimized]:
        assert display(func(init_ll(l), k)) == expected


# Second parameter says where the tail points to again
test_cases = [
    (([3, 2, 0, -4], 1), True),
    (([1, 2], 0), True),
    (([1, 2, 3, 4, 5], -1), False),
    (([1, 2, 3, 4, 5, 4, 2, 3, 1], -1), False),
]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_find_cycle(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in [has_cycle_dict, has_cycle_floyd]:
        assert func(init_ll_cycle(*test_input)) == expected


# Second parameter says where the tail points to again
test_cases = [
    ([1, 2, 3, 4], [1, 4, 2, 3]),
    ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]),
]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_reorder_list(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in [reorder_ll_stack, reorder_ll_rec, reorder_ll_reverse]:
        head = init_ll(test_input)
        func(head)
        assert display(head) == expected


def test_deep_copy():
    print(f"\nFor input [[7,null],[13,0],[11,4],[10,2],[1,0]")
    h1 = ListNodeRandom(7)
    node1 = ListNodeRandom(13)
    node2 = ListNodeRandom(11)
    node3 = ListNodeRandom(10)
    node4 = ListNodeRandom(1)

    h1.nxt = node1
    node1.nxt = node2
    node2.nxt = node3
    node3.nxt = node4

    h1.random = None
    node1.random = h1
    node2.random = node4
    node3.random = node2
    node4.random = h1

    h2 = deep_copy_random_list(h1)

    assert h1 != h2 and h1.nxt.val == h2.nxt.val and h1.nxt != h2.nxt


test_cases = [
    ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
    ([[1, 4, 7, 9, 10], [11, 12, 13, 17], [19, 20, 23, 24]],
     [1, 4, 7, 9, 10, 11, 12, 13, 17, 19, 20, 23, 24]),
    ([], []),
    ([[]], []),
]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_merge_k_lists(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in [merge_k_lists_sort, merge_k_lists_v1, merge_k_lists_v2, merge_k_lists_v3]:
        ll_heads = [init_ll(l) for l in test_input]
        assert display(func(ll_heads)) == expected


test_cases = [
    (([1, 2, 3, 4, 5], 2), [2, 1, 4, 3, 5]),
    (([1, 2, 3, 4, 5], 3), [3, 2, 1, 4, 5]),
    (([1, 2], 2), [2, 1]),
    (([1, 2, 3, 4, 5], 1), [1, 2, 3, 4, 5]),
    (([1, 2, 3, 4], 2), [2, 1, 4, 3]),
]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_reverse_k_group(test_input, expected):
    print(f"\nFor input {test_input}")
    l, k = test_input
    for func in [reverse_k_group_stack, reverse_k_group_backtrack, reverse_k_group_space_optimized, reverse_k_group_space_optimized_v2]:
        assert display(func(init_ll(l), k)) == expected
