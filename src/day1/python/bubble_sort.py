def bubble_sort(arr: list[int]) -> None:
    length = len(arr)
    while length > 0:
        for i in range(length-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        length -= 1
