from calculator import Calculator


def main():
    calculator = Calculator()

    try:
        a = int(input("첫 번째 숫자: "))
        operator = input("연산자 (+, -, *, /): ")
        b = int(input("두 번째 숫자: "))

        if operator == '+':
            print("결과:", calculator.add(a, b))
        elif operator == '-':
            print("결과:", calculator.subtract(a, b))
        elif operator == '*':
            print("결과:", calculator.multiply(a, b))
        elif operator == '/':
            print("결과:", calculator.divide(a, b))
        else:
            print("잘못된 연산자입니다.")
    except ValueError as e:
        print("오류:", str(e))


if __name__ == "__main__":
    main()
