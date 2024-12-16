const Calculator = require('./calculator');
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

const calculator = new Calculator();

function getInput() {
    readline.question('첫 번째 숫자: ', (num1) => {
        readline.question('연산자 (+, -, *, /): ', (operator) => {
            readline.question('두 번째 숫자: ', (num2) => {
                try {
                    const number1 = parseFloat(num1);
                    const number2 = parseFloat(num2);
                    let result;

                    switch (operator) {
                        case '+':
                            result = calculator.add(number1, number2);
                            break;
                        case '-':
                            result = calculator.subtract(number1, number2);
                            break;
                        case '*':
                            result = calculator.multiply(number1, number2);
                            break;
                        case '/':
                            result = calculator.divide(number1, number2);
                            break;
                        default:
                            console.log('잘못된 연산자입니다.');
                            readline.close();
                            return;
                    }
                    console.log(`결과: ${result}`);
                } catch (error) {
                    console.log('오류: ' + error.message);
                }
                readline.close();
            });
        });
    });
}

getInput();