def sort_counting(arr: list[int]) -> list[int]:
    if not arr:
        return arr

    min_val = min(arr)
    max_val = max(arr)
    count = [0]*(max_val-min_val+1)

    # [1,4,9,4,0] -> count=[1,1,0,0,2,0,0,0,0,1]
    for elem in arr:
        count[elem-min_val] += 1

    # count=[1,2,2,2,4,4,4,4,4,5]
    for i in range(1, len(count)):
        count[i] += count[i-1]

    # When going backwards we check where we need to place the current element
    # Example, for number 9, we will do 9 - minimum in that array, what we get is an index
    # Then we check the number at that index in the count array
    # Decrement by 1 and put the number in sorted at that index
    _sorted = [0]*len(arr)
    for num in arr[::-1]:
        count[num-min_val] -= 1
        _sorted[count[num-min_val]] = num

    return _sorted
