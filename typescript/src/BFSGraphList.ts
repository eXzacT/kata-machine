import Queue from "./Queue";

export default function bfs(graph: WeightedAdjacencyList, source: number, needle: number): number[] {
    const seen = new Array(graph.length).fill(false);
    const prev = new Array(graph.length).fill(-1);
    seen[source] = true;

    const q = new Queue();
    q.enqueue(source);

    while (q.length) {
        const curr = q.deque() as number;
        if (curr === needle) {
            break;
        }
        const adjs = graph[curr];
        for (let i = 0; i < adjs.length; i++) {
            const nxt = adjs[i].to
            if (!seen[nxt]) {
                seen[nxt] = true;
                prev[nxt] = curr;
                q.enqueue(nxt)
            }
        }
    }
    if (prev[needle] == -1) {
        return [];
    }

    let curr = needle;
    const out: number[] = [];
    while (prev[curr] !== -1) {
        out.push(curr);
        curr = prev[curr];
    }
    return [source].concat(out.reverse());
}