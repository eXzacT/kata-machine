from typing import Any

if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution


class ListNode:
    def __init__(self, val: Any = 0, nxt: "ListNode" = None) -> None:
        self.val = val
        self.nxt = nxt

    def __repr__(self) -> str:
        return f"<List Node, {self.val}>"


class LinkedList():
    def __init__(self, head: ListNode = None) -> None:
        self.head = head

    def display(self) -> list[Any]:
        curr = self.head
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.nxt

        return res

    def reverse_rec(self) -> None:
        def helper(prev: ListNode, curr: ListNode) -> None:
            if curr.nxt == None:
                curr.nxt = prev
                self.head = curr
                return

            helper(curr, curr.nxt)
            curr.nxt = prev

        helper(None, self.head)

    def reverse(self) -> None:
        prev, curr = None, self.head
        while curr:
            nxt = curr.nxt
            curr.nxt = prev
            prev, curr = curr, nxt

        self.head = prev


def reverse_list(head: ListNode) -> ListNode:
    prev, curr = None, head
    while curr:
        nxt = curr.nxt
        curr.nxt = prev
        prev, curr = curr, nxt

    return prev


def display(head: ListNode) -> list[Any]:
    res = []
    while head:
        res.append(head.val)
        head = head.nxt

    return res


def init_ll(vals: list[Any]) -> ListNode:
    if vals:
        head = ListNode(vals[0])
        curr = head
        for i in range(1, len(vals)):
            curr.nxt = ListNode(vals[i])
            curr = curr.nxt

        return head

    return


''' You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
    Return the head of the merged linked list.'''


def merge_two_sorted_lls(h1: ListNode, h2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy

    while h1 and h2:
        if h2.val < h1.val:
            tail.nxt = h2
            tail = h2
            h2 = h2.nxt
        else:
            tail.nxt = h1
            tail = h1
            h1 = h1.nxt

    if h1:
        tail.nxt = h1
    if h2:
        tail.nxt = h2

    return dummy.nxt


''' You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order, and each of their nodes contains a single digit. 
    Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''


def sum_two_linked_lists(h1: ListNode, h2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy
    carry = 0
    while h1 or h2:
        v1 = h1.val if h1 else 0
        v2 = h2.val if h2 else 0

        _sum = v1+v2+carry
        remainder = _sum % 10
        tail.nxt = ListNode(remainder)

        h1 = h1.nxt if h1 else None
        h2 = h2.nxt if h2 else None
        tail = tail.nxt

        carry = 1 if _sum >= 10 else 0

    if carry:
        tail.nxt = ListNode(1)

    return dummy.nxt


'''Given the head of a linked list, remove the k-th node from the end of the list and return the original head.'''


@time_execution(executions=1)
def remove_nth_from_end_naive(head: ListNode, k: int) -> ListNode:
    curr = head
    length = steps = 0

    # First find out how long the linked list is, later we will know which one kth is from the back
    while curr:
        length += 1
        curr = curr.nxt

    if k == length:  # Have to remove the head
        temp = head.nxt
        head.nxt = None
        return temp

    curr = head
    # Stop when you encounter the node just before k-th
    while steps < length-k-1:
        steps += 1
        curr = curr.nxt

    # Delete the k-th node
    curr.nxt.nxt, curr.nxt = None, curr.nxt.nxt

    return head


@time_execution(executions=1)
def remove_nth_from_end_optimized(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while k > 0 and right:
        k -= 1
        right = right.nxt

    # At any point left pointer is at 1 position just left of a possible target node
    while right:
        right = right.nxt
        left = left.nxt

    # Delete the k-th node
    left.nxt.nxt, left.nxt = None, left.nxt.nxt

    return dummy.nxt
