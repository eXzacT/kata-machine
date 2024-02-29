import re
from collections import deque
if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create(nums: list[int | None]) -> TreeNode:
    if not nums:
        return None

    nodes = [None if num is None else TreeNode(num) for num in nums]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if not kids:
            break
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root


def display(head: TreeNode) -> list:
    bfs = []
    queue = deque([head])

    while queue:
        curr = queue.popleft()
        if not curr:
            bfs.append(None)
            continue

        bfs.append(curr.val)
        queue.append(curr.left)
        queue.append(curr.right)

    # Removing ending Nones
    while bfs and bfs[-1] == None:
        bfs.pop()

    return bfs


def print_tree(root):
    def tree_depth(node):
        if not node:
            return 0
        left_depth = tree_depth(node.left)
        right_depth = tree_depth(node.right)
        return max(left_depth, right_depth) + 1

    def fill_positions(grid, node, depth, pos, offsets):
        if depth + 1 < len(grid):
            if node:
                grid[depth][pos] = str(node.val)
                fill_positions(grid, node.left, depth + 1,
                               pos - offsets[depth + 1], offsets)
                fill_positions(grid, node.right, depth + 1,
                               pos + offsets[depth + 1], offsets)
            else:
                grid[depth][pos] = 'x'

    depth = tree_depth(root)
    width = 2 ** depth - 1
    grid = [[" " for _ in range(width)] for _ in range(depth)]

    offsets = [2 ** (depth - i - 1) for i in range(depth)]
    fill_positions(grid, root, 0, width // 2, offsets)

    tree_str = "\n".join("".join(row) for row in grid)
    return tree_str


'''Given the root of a binary tree, invert the tree, and return its root.'''


@time_execution(executions=1)  # Mutating the tree
def invert_tree_rec(root: TreeNode) -> TreeNode:
    def helper(curr: TreeNode) -> None:
        if not curr:
            return
        curr.left, curr.right = curr.right, curr.left
        helper(curr.left)
        helper(curr.right)

    helper(root)
    return root


@time_execution(executions=1)  # Mutating the tree
def invert_tree_iter(root: TreeNode) -> TreeNode:
    stack = [root]
    while stack:
        curr = stack.pop()
        if not curr:
            continue
        curr.left, curr.right = curr.right, curr.left
        stack.append(curr.left)
        stack.append(curr.right)

    return root


''' Given the root of a binary tree, return its maximum depth.
    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.'''


@time_execution()
def max_depth_dfs(root: TreeNode) -> int:
    def helper(curr: TreeNode) -> int:
        if not curr:
            return 0

        return 1+max(helper(curr.left), helper(curr.right))

    return helper(root)


@time_execution()
def max_depth_dfs_v2(root: TreeNode) -> int:
    def helper(curr: TreeNode, depth: int) -> int:
        if not curr:
            return depth

        return max(helper(curr.left, depth+1), helper(curr.right, depth+1))

    return helper(root, 0)


@time_execution()
def max_depth_iter(root: TreeNode) -> int:
    max_depth = 0
    stack = [(root, 1)]

    while stack:
        curr, depth = stack.pop()
        if not curr:
            continue

        max_depth = max(max_depth, depth)
        stack.append((curr.left, depth+1))
        stack.append((curr.right, depth+1))

    return max_depth


@time_execution()
def max_depth_bfs(root: TreeNode) -> int:
    if not root:
        return 0

    queue = deque([root])
    max_depth = 0

    while queue:
        # Replace every node in current level with its children
        for _ in range(len(queue)):
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        max_depth += 1

    return max_depth


''' Given the root of a binary tree, return the length of the diameter of the tree.
    The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
    This path may or may not pass through the root.
    The length of a path between two nodes is represented by the number of edges between them.'''


@time_execution()
def max_diameter_dfs(root: TreeNode) -> int:
    max_diameter = 0

    def helper(curr: TreeNode) -> int:
        nonlocal max_diameter
        if not curr:
            return 0

        max_left, max_right = helper(curr.left), helper(curr.right)
        max_diameter = max(max_left+max_right, max_diameter)
        return 1+max(max_left, max_right)

    helper(root)
    return max_diameter


@time_execution()
def max_diameter_dfs_v2(root: TreeNode) -> int:
    max_diameter = 0

    def helper(curr: TreeNode, depth: int) -> int:
        nonlocal max_diameter
        if not curr:
            return depth-1  # -1 to subtract parent

        max_left = helper(curr.left, depth+1)
        max_right = helper(curr.right, depth+1)
        # Max depth of left subtree and right subtree(counting from root), that's why we have to subtract current depth twice so it's only the remainder depths for each
        max_diameter = max(max_left+max_right-2*depth, max_diameter)
        return max(max_left, max_right)

    helper(root, 0)
    return max_diameter


'''Given a binary tree, determine if it is height-balanced'''


@time_execution()
def is_balanced_dfs(root: TreeNode) -> bool:
    is_balanced = True

    def helper(curr: TreeNode) -> bool:
        nonlocal is_balanced
        if not curr:
            return 0

        max_left, max_right = helper(curr.left), helper(curr.right)
        if abs(max_left-max_right) > 1:
            is_balanced = False
        return 1+max(max_left, max_right)

    helper(root)
    return is_balanced


@time_execution()
def is_balanced_dfs_v2(root: TreeNode) -> bool:
    is_balanced = True

    def helper(curr: TreeNode, depth: int) -> bool:
        nonlocal is_balanced
        if not curr:
            return depth

        max_left, max_right = helper(
            curr.left, depth+1), helper(curr.right, depth+1)
        if abs(max_left-max_right) > 1:
            is_balanced = False
        return max(max_left, max_right)

    helper(root, 0)
    return is_balanced


''' Given the roots of two binary trees s and t, write a function to check if they are the same or not.
    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.'''


@time_execution()
def is_same_dfs(root1: TreeNode, root2: TreeNode) -> bool:
    def helper(curr1: TreeNode, curr2: TreeNode) -> bool:
        if not curr1 or not curr2:  # Make sure they're both None if one of them is None
            return curr1 == curr2

        return curr1.val == curr2.val and helper(curr1.left, curr2.left) and helper(curr1.right, curr2.right)

    return helper(root1, root2)


@time_execution()
def is_same_iter(root1: TreeNode, root2: TreeNode) -> bool:
    stack = [(root1, root2)]
    while stack:
        curr1, curr2 = stack.pop()
        if not curr1 or not curr2:
            if curr1 == curr2:  # Both None
                continue
            else:  # One of them is not None, return early
                return False

        if curr1.val == curr2.val:
            stack.append((curr1.left, curr2.left))
            stack.append((curr1.right, curr2.right))
        else:
            return False

    return True


@time_execution()
def is_same_bfs(root1: TreeNode, root2: TreeNode) -> bool:
    queue = deque([(root1, root2)])
    while queue:
        curr1, curr2 = queue.popleft()
        if not curr1 or not curr2:
            if curr1 == curr2:  # Both None
                continue
            else:  # One of them is not None, return early
                return False

        if curr1.val == curr2.val:
            queue.append((curr1.left, curr2.left))
            queue.append((curr1.right, curr2.right))
        else:
            return False

    return True


''' Given the roots of two binary trees root and subroot, return true if there is a subtree of root with the same structure 
    and node values of subRoot and false otherwise.
    A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
    The tree tree could also be considered as a subtree of itself.'''


@time_execution()
def is_subtree(s: TreeNode, t: TreeNode) -> bool:
    def is_same(s: TreeNode, t: TreeNode) -> bool:
        if not s or not t:  # Make sure they're both None if one of them is None
            return s == t

        return s.val == t.val and is_same(s.left, t.left) and is_same(s.right, t.right)

    # For every node in 's' check whether the tree below including it is same as tree 't'
    stack = [s]
    while stack:
        curr = stack.pop()
        if is_same(curr, t):
            return True
        else:
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

    return False


@time_execution()
def is_subtree_v2(s: TreeNode, t: TreeNode) -> bool:
    def is_same(s: TreeNode, t: TreeNode) -> bool:
        if not s or not t:  # Make sure they're both None if one of them is None
            return s == t

        return s.val == t.val and is_same(s.left, t.left) and is_same(s.right, t.right)

    def helper(s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        if not s:
            return False

        return is_same(s, t) or helper(s.left, t) or helper(s.right, t)

    return helper(s, t)


''' Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
    The lowest common ancestor is defined between two nodes p and q as the lowest node in T 
    that has both p and q as descendants (where we allow a node to be a descendant of itself).'''


@time_execution()
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    index_map = {0: root}  # Position: Node
    i = j = None

    def helper(node: TreeNode, idx: int):
        nonlocal i, j
        if not node:
            return

        if node.val == p.val:
            i = idx
        elif node.val == q.val:
            j = idx

        index_map[2*idx+1] = node.left
        index_map[2*idx+2] = node.right
        helper(node.left, 2*idx+1)
        helper(node.right, 2*idx+2)

    helper(root, 0)

    # Find the index of LCA by moving up from the child which is deeper until we're at the same position (same ancestor)
    while i != j:
        if i > j:
            i = (i - 1) // 2
        else:
            j = (j - 1) // 2

    return index_map[i]


@time_execution()
def lowest_common_ancestor_v2(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    index_map = {0: root}  # Position: Node
    i = j = None
    queue = deque([(root, 0)])
    while queue:
        curr, idx = queue.popleft()
        if not curr:
            continue

        if curr.val == p.val:
            i = idx
        elif curr.val == q.val:
            j = idx

        if i != None and j != None:
            break

        index_map[2*idx+1] = curr.left
        index_map[2*idx+2] = curr.right
        queue.append((curr.left, 2*idx+1))
        queue.append((curr.right, 2*idx+2))

    # Find the index of LCA by moving up from the child which is deeper until we're at the same position (same ancestor)
    while i != j:
        if i > j:
            i = (i - 1) // 2
        else:
            j = (j - 1) // 2

    return index_map[i]


@time_execution()
def lowest_common_ancestor_v3(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    def helper(curr: TreeNode) -> TreeNode:
        if curr.val < p.val and curr.val < q.val:  # Both nodes are bigger than the current value, search right
            return helper(curr.right)
        if curr.val > p.val and curr.val > q.val:  # Both nodes are smaller than the current value, search left
            return helper(curr.left)
        return curr  # Means current node is equal to one of the current nodes, this is where the split starts

    return helper(root)


'''Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).'''


@time_execution()
def level_order_traversal_iter(root: TreeNode) -> list[list[int]]:
    res = []
    if not root:
        return res

    queue = deque([root])
    while queue:
        curr_level = []
        for _ in range(len(queue)):
            curr = queue.popleft()
            curr_level.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        res.append(curr_level)

    return res


@time_execution()
def level_order_traversal_rec(root: TreeNode) -> list[list[int]]:
    if not root:
        return []
    res = [[]]

    def helper(node: TreeNode, depth: int) -> None:
        if not node:
            return

        if depth < len(res):
            res[depth].append(node.val)
        else:
            res.append([node.val])

        helper(node.left, depth+1)
        helper(node.right, depth+1)

    helper(root, 0)
    return res


''' Given the root of a binary tree, imagine yourself standing on the right side of it, 
    return the values of the nodes you can see ordered from top to bottom. Basically rightmost nodes on every level'''


@time_execution()
def right_side_view_bfs(root: TreeNode) -> list[int]:
    res = []
    if not root:
        return res

    queue = deque([root])
    while queue:
        queue_len = len(queue)
        for i in range(queue_len):
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

            if i == queue_len-1:  # Rightmost node in a level
                res.append(curr.val)

    return res


@time_execution()
def right_side_view_dfs(root: TreeNode) -> list[int]:
    res = []

    def helper(curr: TreeNode, level: int) -> None:
        if not curr:
            return
        if level == len(res):
            # Since we reached the new level just add whatever the node is, it can be a left node if there's no right
            res.append(curr.val)

        # Go right first to prioritize rightmost nodes
        helper(curr.right, level + 1)
        helper(curr.left, level + 1)

    helper(root, 0)
    return res


''' Given a binary tree root, a node X in the tree is named good if in the path from root to X there are 
    no nodes with a value greater than X.
    Return the number of good nodes in the binary tree.'''


@time_execution()
def good_nodes_dfs(root: TreeNode) -> int:
    def helper(curr: TreeNode, count: int, max_val: int) -> int:
        if not curr:
            return count

        if curr.val >= max_val:
            count += 1
            max_val = curr.val

        # Subtracting current count so we don't count it twice, since both paths have that count in them
        return helper(curr.left, count, max_val) + helper(curr.right, count, max_val) - count

    return helper(root, 0, root.val)


@time_execution()
def good_nodes_dfs_v2(root: TreeNode) -> int:
    def helper(curr: TreeNode, max_val: int) -> int:
        if not curr:
            return 0

        if curr.val >= max_val:
            return 1+helper(curr.left, curr.val)+helper(curr.right, curr.val)

        return helper(curr.left, max_val)+helper(curr.right, max_val)

    return helper(root, root.val)


''' Given the root of a binary tree, determine if it is a valid binary search tree (BST).

    A valid BST is defined as follows:

        The left subtree of a node contains only nodes with keys less than the node's key.
        The right subtree of a node contains only nodes with keys greater than the node's key.
        Both the left and right subtrees must also be binary search trees.'''


@time_execution()
def validate_binary_search_tree(root: TreeNode) -> bool:
    def helper(curr: TreeNode, min_val: int, max_val: int) -> bool:
        if not curr:
            return True

        if min_val < curr.val < max_val:
            return helper(curr.left, min_val, curr.val) and helper(curr.right, curr.val, max_val)
        return False

    return helper(root, float('-inf'), float('inf'))


'''Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.'''


@time_execution()
def kth_smallest_inorder_dfs(root: TreeNode, k: int) -> int:
    res = []

    def helper(curr: TreeNode) -> None:
        if not curr:
            return

        helper(curr.left)
        res.append(curr.val)
        helper(curr.right)

    helper(root)
    return res[k-1]


@time_execution()
def kth_smallest_inorder_dfs_v2(root: TreeNode, k: int) -> int:
    steps = 0
    res = None

    def helper(curr: TreeNode):
        nonlocal steps, res
        if not curr or res is not None:  # Already found the result or empty node
            return

        helper(curr.left)
        steps += 1

        if steps == k:
            res = curr.val
            return
        helper(curr.right)

    helper(root)
    return res


@time_execution()
def kth_smallest_inorder_iter(root: TreeNode, k: int) -> int:
    steps = 0
    stack = []
    curr = root

    while curr or stack:
        while curr:  # Keep going left and remember which node we visited
            stack.append(curr)
            curr = curr.left

        # Once we're done going left process the node
        curr = stack.pop()
        steps += 1
        if steps == k:
            return curr.val

        # After processing we can go right
        curr = curr.right


''' Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and 
    inorder is the inorder traversal of the same tree, construct and return the binary tree.'''


@time_execution()
def build_from_preorder_inorder(preorder: list[int], inorder: list[int]) -> TreeNode:
    def helper(preorder: list[int], inorder: list[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = helper(preorder[1:mid+1], inorder[:mid])
        root.right = helper(preorder[mid+1:], inorder[mid+1:])

        return root

    return helper(preorder, inorder)


@time_execution()
def build_from_preorder_inorder_optimized(preorder: list[int], inorder: list[int]) -> TreeNode:
    if not preorder or not inorder:
        return None

    # Mapping of inorder values to their indices for quick access
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    next_idx = 0

    def helper(start: int, end: int) -> TreeNode:
        nonlocal next_idx
        if start > end:
            return None

        # Get the current root value and create the TreeNode
        root = TreeNode(preorder[next_idx])
        next_idx += 1
        mid = inorder_map[root.val]

        # Recursively construct the left and right subtree
        root.left = helper(start, mid - 1)
        root.right = helper(mid + 1, end)

        return root

    return helper(0, len(inorder) - 1)


''' A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
    A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
    The path sum of a path is the sum of the node's values in the path.
    Given the root of a binary tree, return the maximum path sum of any non-empty path.'''


@time_execution()
def max_path_sum(root: TreeNode) -> int:
    res = root.val

    def helper(curr: TreeNode) -> int:
        nonlocal res
        if not curr:
            return 0

        max_left = helper(curr.left)
        max_right = helper(curr.right)
        # Keep them neutral if it's negative, because we don't need to take children nodes into path
        max_left = max(max_left, 0)
        max_right = max(max_right, 0)

        # It's possible that path from left to right node through the current one is best
        # But we can't return that value since that path can't go to the parent of current node
        res = max(res, max_left+max_right+curr.val)

        # Is it better to take the left path or right path?
        best_path = max(max_left, max_right)+curr.val
        return best_path

    helper(root)
    return res


''' Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored 
    in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. 
    You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.'''


@time_execution()
def serialize_binary_tree(root: TreeNode) -> str:
    return str(display(root))


@time_execution()
def deserialize_binary_tree(data: str) -> TreeNode:
    return create([int(val) if val.lstrip('-').isdigit() else None for val in re.findall(r'-?\d+|None', data)])
