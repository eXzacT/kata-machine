from typing import Any


def is_tree(G: dict[Any, list[Any]]) -> bool:
    def dfs(V: Any):
        if V not in visited:
            visited.add(V)
            for E in G[V]:
                edges.append((V, E))
                dfs(E)

    visited = set()
    edges: list[tuple[Any, Any]] = []
    # Get the first key and start dfs from it
    V = next(iter(G))
    dfs(V)

    return len(visited) == len(G) and len(edges) == 2*(len(G)-1)
