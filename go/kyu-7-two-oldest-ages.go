package practice

func Sort(ages []int) {
	if len(ages) < 2 { return }

	for i:= 0; i < len(ages) - 1; i++ {
		minIndex := i

		for j:= i + 1; j < len(ages); j++ {
			if ages[j] < ages[minIndex] {
				minIndex = j
			}
		}

		ages[i], ages[minIndex] = ages[minIndex], ages[i]
	}
}

func TwoOldestAges(ages []int) [2]int {
	Sort(ages)
	return [2]int{ages[len(ages) - 2],ages[len(ages) - 1]}
}

---

package practice_test

import (
	"testing"
	"practice"
)

func TestTwoOldestAges(t *testing.T) {
	ages := []int{10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0}

	expected := [2]int{9, 10}
	actual := practice.TwoOldestAges(ages)

	if expected[0] != actual[0] || expected[1] != actual[1] {
		t.Errorf("Expected: %v, but got %v", expected, actual)
	}
}
