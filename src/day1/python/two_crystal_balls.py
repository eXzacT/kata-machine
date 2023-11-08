from math import floor, sqrt


def two_crystal_balls(breaks: list[bool]) -> int:
    JMP = floor(sqrt(len(breaks)))
    idx = JMP

    # As long as the current element is false keep jumping (08/11/2023)
    while idx < len(breaks) and not breaks[idx]:
        idx += JMP

    idx -= JMP

    # +1 because we want to include the place we decremented from (09/11/2023)
    for i in range(idx, idx+JMP+1):
        if breaks[i]:
            return i
    return -1
