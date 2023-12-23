export function quick_sort(arr: number[]): number[] {
    if (arr.length <= 1) {
        return arr;
    }
    const pivot = arr[0];
    const left = [];
    const right = [];
    for (const num of arr.slice(1, arr.length)) {
        if (num <= pivot) {
            left.push(num);
        } else {
            right.push(num);
        }
    }
    return [...quick_sort(left), pivot, ...quick_sort(right)];
}

export function quick_sort_v2(arr: number[]): void {
    function partition(start: number, end: number): number {
        const pivot = arr[end];
        let pivotIdx = start;
        for (let i = start; i < end; i++) {
            if (arr[i] <= pivot) {
                [arr[i], arr[pivotIdx]] = [arr[pivotIdx], arr[i]];
                pivotIdx++;
            }
        }
        [arr[end], arr[pivotIdx]] = [arr[pivotIdx], pivot];
        return pivotIdx;
    }

    function helper(start: number, end: number): void {
        if (start < end) {
            const pivotIdx = partition(start, end);
            helper(start, pivotIdx - 1);
            helper(pivotIdx + 1, end);
        }
    }
    return helper(0, arr.length - 1);
}