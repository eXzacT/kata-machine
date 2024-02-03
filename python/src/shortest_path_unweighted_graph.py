import networkx as nx
from collections import deque
import heapq

if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution


@time_execution()
def sol_heap(adjacency_list: dict[str, list[str]], source: str, target: str) -> int:
    heap = []
    visited = set()
    heapq.heappush(heap, (0, source, [source]))

    while heap:
        dist, V, path = heapq.heappop(heap)
        visited.add(V)
        for E in adjacency_list[V]:
            if E not in visited:
                if E == target:
                    return path+[E]
                heapq.heappush(heap, (dist+1, E, path+[E]))

    return []


@time_execution()
def sol_bfs(adjacency_list: dict[str, list[str]], source: str, target: str) -> int:
    queue = deque([source])
    prev = {}
    visited = set()
    while queue:
        V = queue.pop()
        visited.add(V)

        if V == target:
            break
        for E in adjacency_list[V]:
            if E not in visited:
                prev[E] = V
                queue.appendleft(E)

    path = [target]
    previous = prev[target]
    while previous:
        path.append(previous)
        previous = prev.get(previous, 0)

    return path[::-1]


@time_execution()
def sol_bfs_v2(adjacency_list: dict[str, list[str]], source: str, target: str) -> int:
    queue = deque([(source, [source])])
    visited = set()

    while queue:
        V, path = queue.pop()
        visited.add(V)

        if V == target:
            return path

        for E in adjacency_list[V]:
            if E not in visited:
                queue.appendleft((E, path+[E]))

    return path


@time_execution()
def sol_nx(adjacency_list: dict[str, list[str]], source: str, target: str) -> int:
    G = nx.DiGraph()
    for V in adjacency_list:
        for E in adjacency_list[V]:
            G.add_edge(V, E)

    return nx.shortest_path(G, source=source, target=target)


G: dict[str, list[str]] = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'I'],
    'C': ['A', 'B', 'F'],
    'D': ['A', 'G'],
    'E': ['C', 'H'],
    'F': ['C', 'H', 'J'],
    'G': ['C', 'D', 'I'],
    'H': ['C', 'E', 'F', 'I'],
    'I': ['B', 'G', 'K'],
    'J': ['F', 'K'],
    'K': ['I', 'J']
}
