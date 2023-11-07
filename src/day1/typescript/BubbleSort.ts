export default function bubble_sort(arr: number[]): void {
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