import { bubble_sort, bubble_sort_rec, bubble_sort_rec_v2 } from "../BubbleSort";

describe("Bubble Sort Tests", () => {
    const testCases = [
        { input: [9, 3, 7, 4, 69, 420, 42], expected: [3, 4, 7, 9, 42, 69, 420] },
        { input: [5, 1, 4, 2, 8], expected: [1, 2, 4, 5, 8] },
        { input: [100, 20, 50, 70, 45], expected: [20, 45, 50, 70, 100] },
        { input: [1], expected: [1] },
        { input: [1, 2], expected: [1, 2] },
        { input: [2, 1], expected: [1, 2] },
        { input: [1, 2, 3, 4, 5], expected: [1, 2, 3, 4, 5] },
        { input: [5, 4, 3, 2, 1], expected: [1, 2, 3, 4, 5] },
        { input: [3, 5, 2, 1, 4], expected: [1, 2, 3, 4, 5] },
        { input: [1, 2, 2, 1, 3, 3, 1, 2, 3], expected: [1, 1, 1, 2, 2, 2, 3, 3, 3] },
        { input: [-1, -2, -3, -4, -5], expected: [-5, -4, -3, -2, -1] },
        { input: [-1, 2, -3, 4, -5], expected: [-5, -3, -1, 2, 4] },
        { input: [], expected: [] },
    ];

    const sortFunctions = [
        { name: "bubble_sort", func: bubble_sort },
        { name: "bubble_sort_rec", func: bubble_sort_rec },
        { name: "bubble_sort_rec_v2", func: bubble_sort_rec_v2 },
    ];

    sortFunctions.forEach(sortFunction => {
        describe(sortFunction.name, () => {
            test.each(testCases)("%o", (testCase) => {
                const arr = [...testCase.input];
                sortFunction.func(arr);
                expect(arr).toEqual(testCase.expected);
            });
        });
    });
});
