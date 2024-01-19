from collections import deque


def topological_sort_dfs(graph: dict[int, list[int]]) -> list[int]:
    visited = set()
    topo_sorted = deque([])

    def helper(v: int):
        if v in visited:
            return

        for e in graph[v]:
            helper(e)

        topo_sorted.appendleft(v)
        visited.add(v)

    for v in graph:
        helper(v)

    # If their lengths are not the same it means we can't possibly sort them topologically
    return list(topo_sorted) if len(topo_sorted) == len(graph) else []


def topological_sort_dfs_v2(graph: dict[int, list[int]]) -> list[int]:
    visited = set()
    topo_sorted = []

    def helper(v: int):
        if v in visited:
            return

        for e in graph[v]:
            helper(e)

        topo_sorted.append(v)
        visited.add(v)

    for v in graph:
        helper(v)

    # If their lengths are not the same it means we can't possibly sort them topologically
    return topo_sorted[::-1] if len(topo_sorted) == len(graph) else []


def topological_sort_bfs(graph: dict[int, list[int]]) -> list[int]:
    topo_sorted = []
    indegree_dict = {v: 0 for v in graph}

    for v in graph:
        for e in graph[v]:
            indegree_dict[e] += 1

    # Add all the verts that have an indegree of 0 to the stack
    stack = [v for v, d in indegree_dict.items() if d == 0]

    while stack:
        v = stack.pop()
        topo_sorted.append(v)

        # Decrease indegree by 1 for each vert that this vert leads to
        for e in graph[v]:
            indegree_dict[e] -= 1
            # Did we visit all the verts that this vert depends on?
            if indegree_dict[e] == 0:
                stack.append(e)

    # If their lengths are not the same it means we can't possibly sort them topologically
    return topo_sorted if len(topo_sorted) == len(graph) else []
