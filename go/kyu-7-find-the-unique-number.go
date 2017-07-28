package practice

func FindUniq(arr []float32) float32 {
	if arr[0] == arr[1] {
		for i:=2; i < len(arr); i++ {
			if arr[i] != arr[0] {
				return arr[i]
			}
		}
 	}

	if arr[2] == arr[0] {
		return arr[1]
	}

	return arr[0]
}

---

package practice_test

import (
	"testing"
	"practice"
)

func TestFindUniq(t *testing.T) {
	arr := []float32{ 1.0, 1.0, 1.0, 2.0, 1.0, 1.0 }

	expected := float32(2)
	actual := practice.FindUniq(arr)

	if actual != expected {
		t.Errorf("Expected: %v, but got %v", expected, actual)
	}
}

func TestFindUniq2(t *testing.T) {
	arr := []float32{ 0, 0, 0.55, 0, 0  }

	expected := float32(0.55)
	actual := practice.FindUniq(arr)

	if actual != expected {
		t.Errorf("Expected: %v, but got %v", expected, actual)
	}
}
