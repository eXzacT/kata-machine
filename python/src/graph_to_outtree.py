from typing import Any


class Node:
    def __init__(self, val: Any):
        self.val = val
        self.children: list['Node'] = []

    def __repr__(self):
        return f"{self.val}"


def tree_to_list_preorder(node: Node) -> list[Node]:
    nodes = []

    def helper(node: Node) -> None:
        nodes.append(node.val)
        for child in node.children:
            helper(child)

    helper(node)
    return nodes


def graph_to_outtree(G: dict[Any, list[Any]], root_val: Any) -> Node:
    def dfs(V: Node) -> None:
        visited.add(V.val)
        for E in G[V.val]:
            if E not in visited:
                child = Node(E)
                V.children.append(child)
                dfs(child)

    root = Node(root_val)
    visited = set()
    dfs(root)

    return root
