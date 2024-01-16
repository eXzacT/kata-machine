def sort_heap(arr: list[int]) -> None:
    def heapify(i: int, end: int) -> None:
        greatest = i
        left = 2*i + 1
        right = 2*i + 2
        if left < end and arr[left] > arr[greatest]:
            greatest = left
        if right < end and arr[right] > arr[greatest]:
            greatest = right
        if i != greatest:
            arr[i], arr[greatest] = arr[greatest], arr[i]
            heapify(greatest, end)

    start = len(arr)//2 - 1
    for i in range(start, -1, -1):
        heapify(i, len(arr))

    for i in range(len(arr)-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(0, i)
