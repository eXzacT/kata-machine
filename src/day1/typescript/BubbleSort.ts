export function bubble_sort(arr: number[]): void {
    let length = arr.length
    while (length > 0) {
        for (let i = 0; i < length - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]]
            }
        }
        length--
    }
}

export function bubble_sort_rec(arr: number[]): void {
    function helper(n: number) {
        if (n <= 1) {
            return;
        }
        for (let i = 0; i < n - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
            }
        }
        helper(n - 1)
    }
    return helper(arr.length);
}

export function bubble_sort_rec_v2(arr: number[]): void {
    function helper(n: number, i: number) {
        if (n <= 1) {
            return;
        }
        if (i == n - 1) {
            i = 0;
            n--;
        }
        if (arr[i] > arr[i + 1]) {
            [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
        }
        helper(n, i + 1);
    }
    helper(arr.length, 0);
}
