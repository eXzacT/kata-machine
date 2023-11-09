package main

func BinarySearchList(haystack []int, needle int) bool {
	lo := 0
	hi := len(haystack)

	for lo < hi {
		mid := lo + (hi-lo)/2

		switch {
		case haystack[mid] == needle:
			return true
		case haystack[mid] < needle:
			lo = mid + 1
		case haystack[mid] > needle:
			hi = mid
		}
	}
	return false
}
