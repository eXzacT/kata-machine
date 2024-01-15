def sort_quick(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []
    for num in arr[1:]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)

    return sort_quick(left)+[pivot]+sort_quick(right)


def sort_quick_v2(arr: list[int]) -> list[int]:
    def partition(start: int, end: int) -> int:
        pivot = arr[end]
        pivot_idx = start
        for i in range(start, end):
            if arr[i] <= pivot:
                arr[i], arr[pivot_idx] = arr[pivot_idx], arr[i]
                pivot_idx += 1

        arr[end], arr[pivot_idx] = arr[pivot_idx], arr[end]
        return pivot_idx

    def helper(start: int, end: int) -> None:
        if start < end:
            pivot = partition(start, end)
            helper(start, pivot-1)
            helper(pivot+1, end)

    helper(0, len(arr)-1)
    return arr


print(sort_quick_v2([5, 1, 9, 2, 50, 20]))
