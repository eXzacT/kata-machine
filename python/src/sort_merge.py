def sort_merge(arr: list[int]) -> list[int]:
    def merge(arr1: list[int], arr2: list[int]) -> list[int]:
        i = j = 0
        merged_arr = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                merged_arr.append(arr1[i])
                i += 1
            else:
                merged_arr.append(arr2[j])
                j += 1

        merged_arr.extend(arr1[i:])
        merged_arr.extend(arr2[j:])
        return merged_arr

    def helper(arr: list[int]) -> list[int]:
        if len(arr) <= 1:
            return arr

        mid = len(arr)//2
        return merge(helper(arr[:mid]), helper(arr[mid:]))

    return helper(arr)
