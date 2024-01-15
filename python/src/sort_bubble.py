def sort_bubble(arr: list[int]) -> None:
    length = len(arr)
    while length > 0:
        for i in range(length-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        length -= 1


def sort_bubble_v2(arr):
    length = len(arr)
    while length > 0:
        swapped = False
        for i in range(length-1):
            if arr[i] > arr[i + 1]:
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        length -= 1
        # If there were no swaps during the entire iteration then it's already sorted
        if not swapped:
            return
