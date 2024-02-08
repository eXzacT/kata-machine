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

functions = [globals()[name] for name in dir() if 'remove' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_remove_nth_from_the_back(test_input, expected):
    print(f"\nFor input {test_input}")
    l, k = test_input
    # Display as a list when given a head reference
    for func in functions:
        assert display(func(init_ll(l), k)) == expected
