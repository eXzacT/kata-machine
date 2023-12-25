package main

import (
	"reflect"
	"testing"
)

func TestBubbleSort(t *testing.T) {
	arr := []int{5, 3, 8, 1}
	BubbleSort(arr)
	expected := []int{1, 3, 5, 8}
	if !reflect.DeepEqual(arr, expected) {
		t.Errorf("BubbleSort() = %v, want %v", arr, expected)
	}
}
