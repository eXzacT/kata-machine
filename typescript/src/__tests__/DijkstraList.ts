import { dijkstra_list, dijkstra_list_v2, dijkstra_min_heap } from "../DijkstraList";
import { list2 } from "./graph";

describe("Dijkstra adjacency list", function () {
    const tests = [
        { name: "dijkstra adj list", func: dijkstra_list },
        { name: "dijkstra adj list v2", func: dijkstra_list_v2 },
        { name: "dijkstra minheap", func: dijkstra_min_heap },
    ];

    for (const test of tests) {
        it(`${test.name} finds path from 0 to 6`, function () {
            expect(test.func(list2, 0, 6)).toEqual([0, 1, 4, 5, 6]);
        });

        it(`${test.name} does not find path from 6 to 0`, function () {
            expect(test.func(list2, 6, 0)).toEqual([]);
        });
    }
});
