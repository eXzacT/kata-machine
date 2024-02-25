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


def init_ll(vals: list[Any]) -> ListNode | None:
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


''' Given head, the head of a linked list, determine if the linked list has a cycle in it.
    There is a cycle in a linked list if there is some node in the list that can be reached again. 

    Return true if there is a cycle in the linked list. Otherwise, return false.'''


def init_ll_cycle(vals: list[Any], tail_pointer: int) -> ListNode:
    head = ListNode(vals[0])
    tail = head
    for i in range(1, len(vals)):
        tail.nxt = ListNode(vals[i])
        tail = tail.nxt

    if tail_pointer != -1:  # If there's a cycle point the tail to node at tail_pointer idx
        curr = head
        for i in range(tail_pointer):
            curr = curr.nxt

        tail.nxt = curr

    return head


@time_execution()
def has_cycle_dict(head: ListNode) -> bool:
    curr = head
    seen = set()

    while curr:
        if curr in seen:
            return True

        seen.add(curr)
        curr = curr.nxt

    return False


@time_execution()
def has_cycle_floyd(head: ListNode) -> bool:
    slow = fast = head

    while fast and fast.nxt:
        slow = slow.nxt
        fast = fast.nxt.nxt

        if slow == fast:
            return True

    return False


''' You are given the head of a singly linked-list. The list can be represented as:
    L0 → L1 → … → Ln - 1 → Ln
    Reorder the list to be on the following form:
    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
    You may not modify the values in the list's nodes. Only nodes themselves may be changed.'''


@time_execution()
def reorder_ll_stack(head: ListNode) -> None:
    stack = []
    curr = head
    while curr:
        stack.append(curr)
        curr = curr.nxt

    for i in range(len(stack)//2):
        temp = stack[i].nxt
        stack[i].nxt = stack[-i-1]
        stack[-i-1].nxt = temp

    stack[len(stack)//2].nxt = None
    return


@time_execution()
def reorder_ll_reverse(head: ListNode) -> None:
    slow = head
    fast = head.nxt
    while fast and fast.nxt:  # First find the middle of the ll
        slow = slow.nxt
        fast = fast.nxt.nxt

    # Reverse the right part, it starts at 1 position right of slow pointer
    prev = None
    right = slow.nxt
    while right:
        temp = right.nxt
        right.nxt = prev
        prev, right = right, temp

    # Now merge them, take 1 from left then 1 from right, and move both pointers inwards
    l, r = head, prev
    while r:
        temp_l, temp_r = l.nxt, r.nxt
        l.nxt = r
        r.nxt = temp_l
        l, r = temp_l, temp_r

    l.nxt = None  # Last left node will now point to None as it will become the last node
    return


@time_execution()
def reorder_ll_rec(head: ListNode) -> None:
    def helper(curr: ListNode) -> None:
        if not curr:
            return

        helper(curr.nxt)
        if not prev:
            return
        p = prev.pop()
        if p == curr or p.nxt == curr:
            curr.nxt = None
            return

        curr.nxt = p.nxt
        prev.append(p.nxt)
        p.nxt = curr

    prev = [head]
    helper(head)
    return


''' A linked list of length n is given such that each node contains an additional random pointer, which could point to any node or null. 
    Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, 
    where each new node has its value set to the value of its corresponding original node. 
    Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers 
    in the original list and copied list represent the same list state. 
    
    None of the pointers in the new list should point to nodes in the original list.
    For example, if there are two nodes X and Y in the original list, 
    where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

    Return the head of the copied linked list.'''


class ListNodeRandom:
    def __init__(self, val: int, nxt: 'ListNodeRandom' = None, random: 'ListNodeRandom' = None):
        self.val = val
        self.nxt = nxt
        self.random = random

    def __repr__(self) -> str:
        return f"<ListNodeRandom val:{self.val}>"


@time_execution()
def deep_copy_random_list(head: ListNodeRandom) -> ListNodeRandom:
    # Because there might be some .random that point to None
    old: dict[int, ListNodeRandom] = {None: None}

    curr = head
    while curr:  # Initialize a new copy for each node, we can't use next or random yet because those nodes might not exist for the moment
        copy = ListNodeRandom(curr.val)
        old[curr] = copy
        curr = curr.nxt

    # Now we can set the next and random pointers
    curr = head
    while curr:
        copy = old[curr]
        copy.nxt = old[curr.nxt]
        copy.random = old[curr.random]
        curr = curr.nxt

    return old[head]


''' You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
    Merge all the linked-lists into one sorted linked-list and return it.'''


@time_execution()
def merge_k_lists_sort(lists: list[ListNode]) -> ListNode:
    dummy = ListNode()
    stack = []

    for head in lists:
        while head:
            stack.append(head.val)
            head = head.nxt

    tail = dummy
    for val in sorted(stack):
        tail.nxt = ListNode(val)
        tail = tail.nxt

    return dummy.nxt


@time_execution(executions=1)  # 1 execution because mutating lists
def merge_k_lists_v1(lists: list[ListNode]) -> ListNode:
    dummy = ListNode()
    tail = dummy

    while any(lists):
        _, idx = min((curr.val, idx) for idx, curr in enumerate(lists) if curr)
        tail.nxt = lists[idx]
        tail = tail.nxt
        lists[idx] = lists[idx].nxt

    return dummy.nxt


@time_execution(executions=1)  # 1 execution because mutating lists
def merge_k_lists_v2(lists: list[ListNode]) -> ListNode:
    if not lists or len(lists) == 0:
        return None

    merged = None
    for i in range(len(lists)):
        merged = merge_two_sorted_lls(merged, lists[i])

    return merged


@time_execution(executions=1)  # 1 execution because mutating lists
def merge_k_lists_v3(lists: list[ListNode]) -> ListNode:
    if not lists or len(lists) == 0:
        return None

    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            # Could be out of range if uneven number
            l2 = lists[i+1] if i+1 < len(lists) else None
            merged.append(merge_two_sorted_lls(l1, l2))

        lists = merged

    return lists[0]


''' Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
    'k' is a positive integer and is less than or equal to the length of the linked list. 
    If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

    You may not alter the values in the list's nodes, only nodes themselves may be changed.'''


@time_execution(executions=1)  # 1 execution because mutating the list
def reverse_k_group_backtrack(head: ListNode, k: int) -> ListNode:
    ''' Yes I am aware the code is very confusing, just wanted to do it using backtracking as practice'''
    def helper(prev: ListNode | None, curr: ListNode | None, length: int) -> ListNode | None:
        nonlocal steps, saved_next, remainder, potential_head, same_length_as_k, last_k_group
        if not curr:
            remainder = length % k
            same_length_as_k = length == k
            return

        helper(curr, curr.nxt, length+1)  # Traverse and find length

        if same_length_as_k:  # Just reverse entire list
            # If first time setting then the head will be last element(which is curr at this time)
            potential_head = potential_head if potential_head else curr
            curr.nxt = prev
            return

        # Backtrack, start changing nodes since there's no remaining portion
        if not remainder:
            if not saved_next:  # At the end of a k-group, have to remember where the end points
                # If potential head exists it means we already reversed some part
                # Because of that the node on the right is no longer curr.nxt but the ending of that k-group
                # And the ending of every k-group is always the potential head
                saved_next = potential_head if potential_head else curr.nxt if curr.nxt else curr
                # EDGE CASE 1, we have to set the nxt to be curr since there is no next
                # This edge case happens when the length is not equal to k but it's a multiple of k
                # Using this boolean flag once to set the first element in that last k-group to point to nothing
                if not curr.nxt:
                    last_k_group = True
                # The last element of a k-group is the new head if it's at the beginning
                potential_head = curr

            steps += 1
            if steps == k:  # At the beginning of a k-group
                # The first node in the k-group will now point where the end was pointing
                if last_k_group:  # EDGE CASE 1
                    curr.nxt = None  # We can't set it to saved_next because it would go in circles
                    last_k_group = False
                else:
                    curr.nxt = saved_next

                steps = 0
                saved_next = None
            else:  # Somewhere in the middle of a k-group, just increment steps and reverse current
                curr.nxt = prev
        else:
            remainder -= 1

    # Edge cases
    if k == 1:  # Don't reverse
        return head

    steps = 0
    remainder = None
    saved_next = None
    potential_head = None
    same_length_as_k = False
    last_k_group = False

    helper(None, head, 0)
    return potential_head


@time_execution(executions=1)  # 1 execution because mutating the list
def reverse_k_group_stack(head: ListNode, k: int) -> ListNode:
    if k == 1:
        return head

    stack = []
    curr = head
    while curr:
        stack.append(curr)
        curr = curr.nxt

    # Skipping remainder, example k=3 but len is 5, leave 4 and 5 intact
    remainder = len(stack) % k
    for i in range(len(stack)-remainder):
        if i % k:  # Not the beginning of a k-group
            stack[i].nxt = stack[i-1]
        else:  # Beginning of a k-group
            stack[i].nxt = stack[i+2*k-1] if i+2*k - 1 < len(stack)\
                else None if not remainder else stack[-remainder]

    # We swapped first with k-1th node so that one is now head
    return stack[k-1]


@time_execution(executions=1)  # 1 execution because mutating the list
def reverse_k_group_space_optimized(head: ListNode, k: int) -> ListNode:
    if k == 1:
        return head

    dummy = ListNode(0, head)
    prev_group_end = dummy

    while True:
        # Check if there are at least k nodes left to reverse
        kth_node = prev_group_end
        for _ in range(k):
            kth_node = kth_node.nxt
            if not kth_node:
                return dummy.nxt

        group_start = prev_group_end.nxt
        next_group_start = kth_node.nxt

        # Reverse the current group of k nodes
        prev = next_group_start
        current = group_start

        for _ in range(k):
            temp = current.nxt
            current.nxt = prev
            prev, current = current, temp

        # Connect the previous group with the reversed group
        prev_group_end.nxt = prev
        prev_group_end = group_start


@time_execution(executions=1)  # 1 execution because mutating the list
def reverse_k_group_space_optimized_v2(head: ListNode, k: int) -> ListNode:
    if k == 1:
        return head

    prev_group_end = dummy = ListNode(0, head)
    l = r = head
    steps = 0

    while r:
        r = r.nxt
        steps += 1
        if steps % k == 0:
            prev = r
            group_start = l
            while r != l:
                temp = l.nxt
                l.nxt = prev
                l, prev = temp, l

            prev_group_end.nxt = prev
            prev_group_end = group_start

    return dummy.nxt
