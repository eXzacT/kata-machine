import { bfs_arr_q, bfs_q } from "../BTBFS";
import { tree } from "./tree";

test("bt bfs array queue", function () {
    expect(bfs_arr_q(tree, 45)).toEqual([true, 10]);
    expect(bfs_arr_q(tree, 7)).toEqual([true, 8]);
    expect(bfs_arr_q(tree, 69)).toEqual([false, -1]);
});

test("bt bfs queue", function () {
    expect(bfs_q(tree, 45)).toEqual([true, 10]);
    expect(bfs_q(tree, 7)).toEqual([true, 8]);
    expect(bfs_q(tree, 69)).toEqual([false, -1]);
});




