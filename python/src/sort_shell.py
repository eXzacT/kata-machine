def sort_shell(arr: list[int]) -> None:
    gap = len(arr)//2
    while gap > 0:
        for i in range(gap, len(arr)):
            val = arr[i]
            j = i
            while j >= gap and arr[j-gap] > val:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = val
        gap //= 2
