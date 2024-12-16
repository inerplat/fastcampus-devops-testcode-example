package calculator

import "testing"

func TestComplexCalculation(t *testing.T) {
    // (10 + 5) * 2 = 30
    result1 := Add(10, 5)
    if got := Multiply(result1, 2); got != 30 {
        t.Errorf("Complex calculation 1 = %v; want 30", got)
    }

    // (20 - 5) / 3 = 5
    result2 := Subtract(20, 5)
    got, err := Divide(result2, 3)
    if err != nil || got != 5.0 {
        t.Errorf("Complex calculation 2 = %v; want 5.0", got)
    }
}