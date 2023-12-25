package main

import (
	rand "math/rand"
	"testing"
)

func TestTwoCrystalBalls(t *testing.T) {
	idx := rand.Intn(10000)
	var data [10000]bool
	var data2 [821]bool
	var data3 [10]bool
	var data4 [9]bool

	for i := idx; i < 10000; i++ {
		data[i] = true
	}

	data3[9] = true

	for i := 6; i < 9; i++ {
		data4[i] = true
	}

	result := TwoCrystalBalls(data[:])
	expected := idx
	if result != expected {
		t.Errorf("Expected %d, but got %d", expected, result)
	}

	result = TwoCrystalBalls(data2[:])
	expected = -1
	if result != expected {
		t.Errorf("Expected %d, but got %d", expected, result)
	}

	result = TwoCrystalBalls(data3[:])
	expected = 9
	if result != expected {
		t.Errorf("Expected %d, but got %d", expected, result)
	}

	result = TwoCrystalBalls(data4[:])
	expected = 6
	if result != expected {
		t.Errorf("Expected %d, but got %d", expected, result)
	}
}
