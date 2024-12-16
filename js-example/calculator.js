class Calculator {
    add(a, b) {
        return a + b;
    }

    subtract(a, b) {
        return a - b;
    }

    multiply(a, b) {
        return a * b;
    }

    divide(a, b) {
        if (b === 0) {
            throw new Error("0으로 나눌 수 없습니다.");
        }
        return a / b;
    }
}

module.exports = Calculator;