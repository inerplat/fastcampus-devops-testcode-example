package calculator

import "testing"

func TestAdd(t *testing.T) {
    if got := Add(2, 3); got != 5 {
        t.Errorf("Add(2, 3) = %v; want 5", got)
    }
    if got := Add(-4, 3); got != -1 {
        t.Errorf("Add(-4, 3) = %v; want -1", got)
    }
}

func TestSubtract(t *testing.T) {
    if got := Subtract(2, 3); got != -1 {
        t.Errorf("Subtract(2, 3) = %v; want -1", got)
    }
    if got := Subtract(-4, 3); got != -7 {
        t.Errorf("Subtract(-4, 3) = %v; want -7", got)
    }
}

func TestMultiply(t *testing.T) {
    if got := Multiply(2, 3); got != 6 {
        t.Errorf("Multiply(2, 3) = %v; want 6", got)
    }
    if got := Multiply(-4, 3); got != -12 {
        t.Errorf("Multiply(-4, 3) = %v; want -12", got)
    }
}

func TestDivide(t *testing.T) {
    got, err := Divide(6, 3)
    if err != nil || got != 2.0 {
        t.Errorf("Divide(6, 3) = %v; want 2.0", got)
    }

    got, err = Divide(-6, 3)
    if err != nil || got != -2.0 {
        t.Errorf("Divide(-6, 3) = %v; want -2.0", got)
    }

    _, err = Divide(4, 0)
    if err == nil {
        t.Error("Divide(4, 0) expected error")
    }
}