package main

func BubbleSort(arr []int) {
	length := len(arr)
	for length > 0 {
		for i := 0; i < length-1; i++ {
			if arr[i] > arr[i+1] {
				arr[i], arr[i+1] = arr[i+1], arr[i]
			}
		}
		length--
	}
}
