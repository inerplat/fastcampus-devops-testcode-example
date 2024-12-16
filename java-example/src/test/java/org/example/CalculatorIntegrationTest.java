package org.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CalculatorIntegrationTest {
    private final Calculator calculator = new Calculator();

    @Test
    void testComplexCalculation() {
        // (10 + 5) * 2 = 30
        int result1 = calculator.add(10, 5);
        assertEquals(30, calculator.multiply(result1, 2));

        // (20 - 5) / 3 = 5
        int result2 = calculator.subtract(20, 5);
        assertEquals(5.0, calculator.divide(result2, 3));
    }
}