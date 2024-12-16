package org.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CalculatorTest {
    private final Calculator calculator = new Calculator();

    @Test
    void add() {
        assertEquals(5, calculator.add(2, 3));
        assertEquals(-1, calculator.add(-4, 3));
    }

    @Test
    void subtract() {
        assertEquals(-1, calculator.subtract(2, 3));
        assertEquals(-7, calculator.subtract(-4, 3));
    }

    @Test
    void multiply() {
        assertEquals(6, calculator.multiply(2, 3));
        assertEquals(-12, calculator.multiply(-4, 3));
    }

    @Test
    void divide() {
        assertEquals(2.0, calculator.divide(6, 3));
        assertEquals(-2.0, calculator.divide(-6, 3));
        assertThrows(IllegalArgumentException.class, () -> calculator.divide(4, 0));
    }
}