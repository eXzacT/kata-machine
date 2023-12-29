import { dfs, dfs_v2, dfs_v3, dfs_iter, dfs_iter_v2 } from "../DFSGraphList";
import { list2 } from "./graph";

describe("DFS - graph", function () {
    const tests = [
        { name: "dfs", func: dfs },
        { name: "dfs_v2", func: dfs_v2 },
        { name: "dfs_v3", func: dfs_v3 },
        { name: "dfs_iter", func: dfs_iter },
        { name: "dfs_iter_v2", func: dfs_iter_v2 },
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
