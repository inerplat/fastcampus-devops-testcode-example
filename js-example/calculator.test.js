const {describe, test, expect} = require('@jest/globals');
const Calculator = require("./calculator");

describe('Calculator', () => {
    const calculator = new Calculator();

    test('add', () => {
        expect(calculator.add(2, 3)).toBe(5);
        expect(calculator.add(-4, 3)).toBe(-1);
    });

    test('subtract', () => {
        expect(calculator.subtract(2, 3)).toBe(-1);
        expect(calculator.subtract(-4, 3)).toBe(-7);
    });

    test('multiply', () => {
        expect(calculator.multiply(2, 3)).toBe(6);
        expect(calculator.multiply(-4, 3)).toBe(-12);
    });

    test('divide', () => {
        expect(calculator.divide(6, 3)).toBe(2.0);
        expect(calculator.divide(-6, 3)).toBe(-2.0);
        expect(() => calculator.divide(4, 0)).toThrow('0으로 나눌 수 없습니다.');
    });
});