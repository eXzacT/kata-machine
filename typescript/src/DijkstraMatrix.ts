import MinHeap from "./MinHeapTuple";

export function dijkstra_matrix(graph: WeightedAdjacencyMatrix, source: number, needle: number): number[] {
    const prev: number[] = new Array(graph.length).fill(-1);
    const seen: boolean[] = new Array(graph.length).fill(false);
    const dists: number[] = new Array(graph.length).fill(Infinity);
    dists[source] = 0;

    while (dists.some((dist, i) => !seen[i] && dist !== Infinity)) {
        const unvisited = dists.map((dist, i) => seen[i] ? Infinity : dist);
        const curr = unvisited.indexOf(Math.min(...unvisited));
        seen[curr] = true;

        const edges = graph[curr];
        for (let i = 0; i < edges.length; i++) {
            if (edges[i] != 0) {
                const dist = dists[curr] + edges[i]
                if (dist < dists[i]) {
                    prev[i] = curr;
                    dists[i] = dist;
                }
            }
        }
    }

    const out: number[] = [];
    if (prev[needle] === -1) {
        return out;
    }

    let curr = needle;
    while (prev[curr] !== -1) {
        out.push(curr)
        curr = prev[curr];
    }
    out.push(source);
    return out.reverse();
}

export function dijkstra_matrix_v2(graph: WeightedAdjacencyMatrix, source: number, needle: number): number[] {
    const paths: number[][] = new Array(graph.length).fill([]);
    const seen: boolean[] = new Array(graph.length).fill(false);
    const dists: number[] = new Array(graph.length).fill(Infinity);
    paths[source] = [source];
    dists[source] = 0;

    while (dists.some((dist, i) => !seen[i] && dist !== Infinity)) {
        const unvisited = dists.map((dist, i) => seen[i] ? Infinity : dist);
        const curr = unvisited.indexOf(Math.min(...unvisited));
        seen[curr] = true;

        const edges = graph[curr];
        for (let i = 0; i < edges.length; i++) {
            if (edges[i] != 0) {
                const dist = dists[curr] + edges[i]
                if (dist < dists[i]) {
                    paths[i] = paths[curr].concat(i);
                    dists[i] = dist;
                }
            }
        }
    }

    return paths[needle];
}

export function dijkstra_matrix_heap(graph: WeightedAdjacencyMatrix, source: number, needle: number): number[] {
    const seen: boolean[] = new Array(graph.length).fill(false);
    const paths: number[][] = new Array(graph.length).fill([]);
    const dists: number[] = new Array(graph.length).fill(Infinity);
    paths[source] = [source];
    dists[source] = 0;

    const heap = new MinHeap();
    heap.push({ node: source, dist: 0 });

    while (heap.length) {
        const { node, dist } = heap.pop()!;
        if (seen[node]) {
            continue;
        }
        seen[node] = true;

        const edges = graph[node];
        for (let i = 0; i < edges.length; i++) {
            if (edges[i] != 0 && !seen[i]) {
                const newDist = edges[i] + dist;
                if (newDist < dists[i]) {
                    dists[i] = newDist;
                    paths[i] = paths[node].concat(i);
                    heap.push({ node: i, dist: newDist });
                }
            }
        }
    }
    return paths[needle];
}