const { describe, test, expect } = require('@jest/globals');
const Calculator = require("./calculator");

describe('Calculator Integration', () => {
    const calculator = new Calculator();

    test('complex calculations', () => {
        // (10 + 5) * 2 = 30
        const result1 = calculator.add(10, 5);
        expect(calculator.multiply(result1, 2)).toBe(30);

        // (20 - 5) / 3 = 5
        const result2 = calculator.subtract(20, 5);
        expect(calculator.divide(result2, 3)).toBe(5.0);
    });
});