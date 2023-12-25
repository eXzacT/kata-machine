export function insertion_sort(arr: number[]): void {
    for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            let j = i;
            while (arr[j + 1] < arr[j] && j >= 0) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
                j--;
            }
        }
    }
}

export function insertion_sort_v2(arr: number[]): void {
    for (let i = 0; i < arr.length; i++) {
        let j = i;
        while (j > 0 && arr[j] < arr[j - 1]) {
            [arr[j], arr[j - 1]] = [arr[j - 1], arr[j]];
            j--;
        }
    }
}

export function insertion_sort_rec(arr: number[]): void {
    function helper(i: number) {
        if (i == arr.length) {
            return;
        }
        if (arr[i - 1] > arr[i]) {
            let j = i;
            while (arr[j + 1] < arr[j] && j >= 0) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
                j--;
            }
        }
        helper(i + 1);
    }
    return helper(0);
}

export function insertion_sort_rec_v2(arr: number[]): void {
    function helper(i: number) {
        if (i < arr.length) {
            let j = i;
            while (j > 0 && arr[j] < arr[j - 1]) {
                [arr[j], arr[j - 1]] = [arr[j - 1], arr[j]];
                j--;
            }
            helper(i + 1);
        }
    }
    helper(0);
}