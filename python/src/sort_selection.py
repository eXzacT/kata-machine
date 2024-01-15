def sort_selection(arr: list[int]) -> None:
    for i in range(len(arr)):
        min_pos = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_pos]:
                min_pos = j

        arr[i], arr[min_pos] = arr[min_pos], arr[i]
