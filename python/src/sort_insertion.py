def sort_insertion(arr: list[int]) -> None:
    for i in range(1, len(arr)):
        j = i
        # Keep swapping until we either reach the beginning or the left part is sorted
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
