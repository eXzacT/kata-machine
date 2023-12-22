import { quick_sort, quick_sort_v2 } from "@code/typescript/QuickSort";

test("quick-sort", function () {
    const arr = [9, 3, 7, 4, 69, 420, 42, 2, 2, 3, 4, 1, 23, 9, 9, 81, 2, 3];

    debugger;
    expect(quick_sort(arr)).toEqual([1, 2, 2, 2, 3, 3, 3, 4, 4, 7, 9, 9, 9, 23, 42, 69, 81, 420]);
});

test("quick-sort_v2", function () {
    const arr2 = [9, 3, 7, 4, 69, 420, 42, 2, 2, 3, 4, 1, 23, 9, 9, 81, 2, 3];
    quick_sort_v2(arr2);
    expect(arr2).toEqual([1, 2, 2, 2, 3, 3, 3, 4, 4, 7, 9, 9, 9, 23, 42, 69, 81, 420]);
});