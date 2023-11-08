package main

import "math"

func TwoCrystalBalls(breaks []bool) int {
	var jmp int = int(math.Sqrt(
		float64(len(breaks))))
	idx := jmp

	for ; idx < len(breaks); idx += jmp {
		if breaks[idx] {
			break
		}
	}

	idx -= jmp

	for ; idx < idx+jmp+1 && idx < len(breaks); idx++ {
		if breaks[idx] {
			return idx
		}
	}
	return -1
}
