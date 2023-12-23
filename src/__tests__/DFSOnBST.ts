import { dfs_iter, dfs_rec } from "@code/typescript/DFSOnBST";
import { tree } from "./tree";

test("DFS on BST", function () {
    expect(dfs_iter(tree, 45)).toEqual(true);
    expect(dfs_iter(tree, 7)).toEqual(true);
    expect(dfs_iter(tree, 69)).toEqual(false);
});

test("DFS on BST rec", function () {
    expect(dfs_rec(tree, 45)).toEqual(true);
    expect(dfs_rec(tree, 7)).toEqual(true);
    expect(dfs_rec(tree, 69)).toEqual(false);
});





