import { compare_iter, compare_rec } from "../CompareBinaryTrees";
import { tree, tree2 } from "./tree";

test("Compare binary trees iteratively", function () {
    expect(compare_iter(tree, tree)).toEqual(true);
    expect(compare_iter(tree, tree2)).toEqual(false);
});

test("Compare binary trees recursively", function () {
    expect(compare_rec(tree, tree)).toEqual(true);
    expect(compare_rec(tree, tree2)).toEqual(false);
});





