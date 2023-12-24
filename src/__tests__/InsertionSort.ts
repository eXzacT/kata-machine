import { insertion_sort, insertion_sort_rec, insertion_sort_rec_v2, insertion_sort_v2 } from "@code/typescript/InsertionSort";

const testCases = [
    { name: "insertion-sort", func: insertion_sort },
    { name: "insertion-sort-v2", func: insertion_sort_v2 },
    { name: "insertion-sort-rec", func: insertion_sort_rec },
    { name: "insertion-sort-rec-v2", func: insertion_sort_rec_v2 }
];

const testArrays = [
    { input: [9, 3, 7, 4, 69, 420, 42], output: [3, 4, 7, 9, 42, 69, 420] },
    { input: [1, 2, 3, 4, 5], output: [1, 2, 3, 4, 5] },
    { input: [5, 4, 3, 2, 1], output: [1, 2, 3, 4, 5] },
    { input: [], output: [] },
    { input: [1], output: [1] }
];

describe.each(testCases)("%s", ({ name, func }) => {
    it.each(testArrays)("should sort the array in ascending order", ({ input, output }) => {
        func(input);
        expect(input).toEqual(output);
    });
});
