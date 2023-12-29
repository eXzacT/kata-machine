export function dfs(graph: WeightedAdjacencyList, source: number, needle: number): number[] {
    function walk(curr: number, seen: boolean[], path: number[]): number[] {
        if (curr == needle) {
            path.push(needle)
            return path;
        }
        if (seen[curr]) {
            return [];
        }
        seen[curr] = true;

        for (const nxt of graph[curr]) {
            const res = walk(nxt.to, seen, path.concat(curr));
            if (res.length) {
                return res;
            }
        }
        return [];
    }
    return walk(source, new Array(graph.length).fill(false), []);
}

export function dfs_v2(graph: WeightedAdjacencyList, source: number, needle: number): number[] {
    function walk(curr: number, path: number[]): boolean {
        if (seen[curr]) {
            return false;
        }

        seen[curr] = true;
        path.push(curr)
        if (curr === needle) {
            return true;
        }

        const list = graph[curr]
        for (const edge of list) {
            if (walk(edge.to, path)) {
                return true;
            }
        }
        path.pop()
        return false;
    }

    const path: number[] = [];
    const seen = new Array(graph.length).fill(false);
    walk(source, path);
    return path;
}

export function dfs_v3(graph: WeightedAdjacencyList, source: number, needle: number): number[] {
    function walk(curr: number): number[] {
        if (curr == needle) {
            return [needle];
        }
        if (seen[curr]) {
            return [];
        }
        seen[curr] = true;

        for (const nxt of graph[curr]) {
            const path = walk(nxt.to);
            if (path.length) {
                return [curr].concat(path);
            }
        }
        return [];
    }
    const seen = new Array(graph.length).fill(false)
    return walk(source);
}

export function dfs_iter(graph: WeightedAdjacencyList, source: number, needle: number): number[] {
    const seen = new Array(graph.length).fill(false);
    const stack: Array<[number, number[]]> = [[source, []]]

    while (stack.length) {
        const [curr, path] = stack.pop()!
        if (curr === needle) {
            path.push(curr);
            return path;
        }
        if (!seen[curr]) {
            seen[curr] = true;
            for (const edge of graph[curr]) {
                stack.push([edge.to, path.concat(curr)]);
            }
        }
    }
    return [];
}

export function dfs_iter_v2(graph: WeightedAdjacencyList, source: number, needle: number): number[] {
    const seen = new Array(graph.length).fill(false);
    const path: number[] = []; // Single shared path array
    const stack: number[] = [source];

    while (stack.length) {
        const curr = stack.pop()!;
        // Keep popping verts that don't lead to this current vert as we already found they don't lead to the needle
        while (path.length && !graph[path[path.length - 1]].some(edge => edge.to === curr)) {
            path.pop();
        }
        if (curr === needle) {
            path.push(curr);
            return path;
        }
        if (!seen[curr]) {
            seen[curr] = true;
            path.push(curr);

            for (const edge of graph[curr]) {
                stack.push(edge.to);
            }
        }
    }
    return [];
}
