from collections import deque, defaultdict


def distance_k_tree_dfs(adjancency_list: dict[str, list[str]], start: str, k: int) -> set[str]:
    # Create the new dictionary where we can also go to parents, not just children
    neighbours_dict = defaultdict(list)
    for V in adjancency_list:
        for E in adjancency_list[V]:
            neighbours_dict[V].append(E)
            neighbours_dict[E].append(V)

    queue = [(start, 0)]
    visited = set()
    nodes_with_dist_k = []

    while queue:
        V, dist = queue.pop()

        if dist == k:
            nodes_with_dist_k.append(V)
            continue

        visited.add(V)
        for E in neighbours_dict[V]:
            if E not in visited:
                queue.append((E, dist+1))

    # Returning set just to avoid traversal order differences, the point is that all the nodes are there
    return set(nodes_with_dist_k)


def distance_k_tree_bfs(adjancency_list: dict[str, list[str]], start: str, k: int) -> set[str]:
    # Create the new dictionary where we can also go to parents, not just children
    neighbours_dict = defaultdict(list)
    for V in adjancency_list:
        for E in adjancency_list[V]:
            neighbours_dict[V].append(E)
            neighbours_dict[E].append(V)

    queue = deque([(start, 0)])
    visited = set()
    nodes_with_dist_k = []

    while queue:
        V, dist = queue.pop()

        if dist == k:
            nodes_with_dist_k.append(V)
            continue

        visited.add(V)
        for E in neighbours_dict[V]:
            if E not in visited:
                queue.appendleft((E, dist+1))

    # Returning set just to avoid traversal order differences, the point is that all the nodes are there
    return set(nodes_with_dist_k)
