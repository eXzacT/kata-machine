import MinHeap from "./MinHeapTuple";

export function dijkstra_list(graph: WeightedAdjacencyList, source: number, needle: number): number[] {
    const prev: number[] = new Array(graph.length).fill(-1);
    const dists: number[] = new Array(graph.length).fill(Infinity);
    const seen: boolean[] = new Array(graph.length).fill(false);
    dists[source] = 0;

    while (dists.some((dist, i) => dist !== Infinity && !seen[i])) {
        const unvisitedDists = dists.map((dist, i) => seen[i] ? Infinity : dist);
        const curr = unvisitedDists.indexOf(Math.min(...unvisitedDists));
        seen[curr] = true;
        for (const edge of graph[curr]) {
            if (!seen[edge.to]) {
                const dist = dists[curr] + edge.weight;
                if (dist < dists[edge.to]) {
                    prev[edge.to] = curr;
                    dists[edge.to] = dist;
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
        out.push(curr);
        curr = prev[curr];
    }
    out.push(source);
    return out.reverse();
}

export function dijkstra_list_v2(graph: WeightedAdjacencyList, source: number, needle: number): number[] {
    const dists: number[] = new Array(graph.length).fill(Infinity);
    const seen: boolean[] = new Array(graph.length).fill(false);
    const paths: number[][] = new Array(graph.length).fill([]);
    paths[source] = [source];
    dists[source] = 0;

    while (dists.some((dist, i) => dist !== Infinity && !seen[i])) {
        const unvisitedDists = dists.map((dist, i) => seen[i] ? Infinity : dist);
        const curr = unvisitedDists.indexOf(Math.min(...unvisitedDists));
        seen[curr] = true;

        for (const edge of graph[curr]) {
            if (!seen[edge.to]) {
                const dist = dists[curr] + edge.weight;
                if (dist < dists[edge.to]) {
                    paths[edge.to] = paths[curr].concat(edge.to);
                    dists[edge.to] = dist;
                }
            }
        }
    }
    return paths[needle];
}

export function dijkstra_min_heap(graph: WeightedAdjacencyList, source: number, needle: number): number[] {
    const seen: boolean[] = new Array(graph.length).fill(false);
    const dists: number[] = new Array(graph.length).fill(Infinity);
    const paths: number[][] = new Array(graph.length).fill([]);
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

        for (const edge of graph[node]) {
            if (!seen[edge.to]) {
                const newDist = dist + edge.weight;
                if (newDist < dists[edge.to]) {
                    dists[edge.to] = newDist;
                    paths[edge.to] = paths[node].concat(edge.to);
                    heap.push({ node: edge.to, dist: newDist });
                }
            }
        }
    }
    return paths[needle];
}