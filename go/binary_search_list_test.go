package main

import (
	"reflect"
	"testing"
)

func TestBinarySearchList(t *testing.T) {
	foo := []int{1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420}

	res := BinarySearchList(foo, 69)
	expected := true
	if !reflect.DeepEqual(res, expected) {
		t.Errorf("BinarySearchList() = %v, want %v", res, expected)
	}

	res = BinarySearchList(foo, 1336)
	expected = false
	if !reflect.DeepEqual(res, expected) {
		t.Errorf("BinarySearchList() = %v, want %v", res, expected)
	}

	res = BinarySearchList(foo, 69420)
	expected = true
	if !reflect.DeepEqual(res, expected) {
		t.Errorf("BinarySearchList() = %v, want %v", res, expected)
	}

	res = BinarySearchList(foo, 69421)
	expected = false
	if !reflect.DeepEqual(res, expected) {
		t.Errorf("BinarySearchList() = %v, want %v", res, expected)
	}

	res = BinarySearchList(foo, 1)
	expected = true
	if !reflect.DeepEqual(res, expected) {
		t.Errorf("BinarySearchList() = %v, want %v", res, expected)
	}

	res = BinarySearchList(foo, 0)
	expected = false
	if !reflect.DeepEqual(res, expected) {
		t.Errorf("BinarySearchList() = %v, want %v", res, expected)
	}
}
