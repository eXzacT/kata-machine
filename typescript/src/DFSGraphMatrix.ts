export function dfs_iter(graph: WeightedAdjacencyMatrix, source: number, needle: number): number[] {
    const seen = new Array(graph.length).fill(false);
    const stack: Array<[number, number[]]> = [[source, []]];

    while (stack.length) {
        const [curr, path] = stack.pop()!
        if (curr === needle) {
            path.push(needle);
            return path;
        }
        if (!seen[curr]) {
            seen[curr] = true;

            const list = graph[curr]
            for (let i = 0; i < list.length; i++) {
                if (list[i] != 0) {
                    stack.push([i, path.concat(curr)]);
                }
            }
        }
    }
    return [];
}

export function dfs_iter_v2(graph: WeightedAdjacencyMatrix, source: number, needle: number): number[] {
    const seen = new Array(graph.length).fill(false);
    const stack: number[] = [source];
    const path: number[] = []; // Single shared array unlike previous version

    while (stack.length) {
        const curr = stack.pop()!
        // Keep popping verts that don't lead to this current vert as we already found they don't lead to the needle
        while (path.length && graph[path[path.length - 1]][curr] === 0) {
            path.pop();
        }

        if (curr === needle) {
            path.push(needle);
            return path;
        }
        if (!seen[curr]) {
            seen[curr] = true;
            path.push(curr);

            const list = graph[curr]
            for (let i = 0; i < list.length; i++) {
                if (list[i] != 0) {
                    stack.push(i);
                }
            }
        }
    }
    return [];
}

export function dfs(graph: WeightedAdjacencyMatrix, source: number, needle: number): number[] {
    function walk(curr: number, path: number[]): boolean {
        if (seen[curr]) {
            return false;
        }

        seen[curr] = true;
        path.push(curr)
        if (curr === needle) {
            return true;
        }

        for (let i = 0; i < graph.length; i++) {
            if (graph[curr][i] != 0) {
                if (walk(i, path)) {
                    return true;
                }
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

export function dfs_v2(graph: WeightedAdjacencyMatrix, source: number, needle: number): number[] {
    function walk(curr: number, seen: boolean[]): number[] {
        if (curr === needle) {
            return [needle];
        }
        if (seen[curr]) {
            return [];
        }

        seen[curr] = true;
        const list = graph[curr]
        for (let i = 0; i < list.length; i++) {
            if (graph[curr][i] != 0) {
                const path = walk(i, seen);
                if (path.length) {
                    return [curr].concat(path);
                }
            }
        }
        return [];
    }

    const seen = new Array(graph.length).fill(false);
    return walk(source, seen);
}