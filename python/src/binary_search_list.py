def binary_search_list(haystack: list[int], needle: int) -> bool:
    hi = len(haystack)
    lo = 0

    while lo < hi:
        MID = int(lo+(hi-lo)/2)

        if haystack[MID] == needle:
            return True

        if haystack[MID] < needle:
            lo = MID+1
        else:
            hi = MID

    return False
