import { dijkstra_matrix, dijkstra_matrix_v2, dijkstra_matrix_heap } from "../DijkstraMatrix";
import { matrix2 } from "./graph";

describe("DijkstraMatrix", function () {
    const tests = [
        { name: "dijkstra_matrix", func: dijkstra_matrix },
        { name: "dijkstra_matrix_v2", func: dijkstra_matrix_v2 },
        { name: "dijkstra_matrix_heap", func: dijkstra_matrix_heap },
    ];

    for (const test of tests) {
        it(`${test.name} finds path from 0 to 6`, function () {
            expect(test.func(matrix2, 0, 6)).toEqual([0, 1, 4, 5, 6]);
        });

        it(`${test.name} does not find path from 6 to 0`, function () {
            expect(test.func(matrix2, 6, 0)).toEqual([]);
        });
    }
});
