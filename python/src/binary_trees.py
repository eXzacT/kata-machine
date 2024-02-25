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
            continue

        bfs.append(curr.val)
        queue.append(curr.left)
        queue.append(curr.right)

    return bfs


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


''' Given the roots of two binary trees p and q, write a function to check if they are the same or not.
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
