def topological_sort_dfs(graph: dict[int, list[int]]) -> list[int]:
    UNVISITED = 0
    VISITING = 1
    VISITED = 2

    visited = {v: UNVISITED for v in graph}
    topo_sorted = []

    def helper(v: int) -> bool:
        if visited[v] == VISITED:
            return True
        if visited[v] == VISITING:  # Cycle
            return False

        visited[v] = VISITING

        for e in graph[v]:
            if not helper(e):
                return False

        visited[v] = VISITED
        topo_sorted.append(v)
        return True

    for v in graph:
        if not helper(v):
            return []  # There was a cycle so we can't topologically sort the graph

    return topo_sorted[::-1]


def topological_sort_dfs_v2(graph: dict[int, list[int]]) -> list[int]:
    visited = set()
    current_path = set()
    topo_sorted = []

    def helper(v: int) -> bool:
        if v in visited:
            return True
        if v in current_path:  # Cycle
            return False

        current_path.add(v)

        for e in graph[v]:
            if not helper(e):
                return False

        current_path.remove(v)
        topo_sorted.append(v)
        visited.add(v)
        return True

    for v in graph:
        if not helper(v):
            return []  # There was a cycle so we can't topologically sort the graph

    return topo_sorted[::-1]


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
