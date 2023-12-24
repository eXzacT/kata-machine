import merge_sort from "@code/typescript/MergeSort";

const testArrays = [
    { input: [9, 3, 7, 4, 69, 420, 42], output: [3, 4, 7, 9, 42, 69, 420] },
    { input: [1, 2, 3, 4, 5], output: [1, 2, 3, 4, 5] },
    { input: [5, 4, 3, 2, 1], output: [1, 2, 3, 4, 5] },
    { input: [], output: [] },
    { input: [1], output: [1] }
];

it.each(testArrays)("should sort the array in ascending order", ({ input, output }) => {
    expect(merge_sort(input)).toEqual(output);
});