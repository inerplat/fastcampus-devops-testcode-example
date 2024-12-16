package main

import (
	"fmt"
	"go-example/calculator"
)

func main() {
    var a, b int
    var operator string

    fmt.Print("첫 번째 숫자: ")
    fmt.Scan(&a)
    fmt.Print("연산자 (+, -, *, /): ")
    fmt.Scan(&operator)
    fmt.Print("두 번째 숫자: ")
    fmt.Scan(&b)

    switch operator {
    case "+":
        fmt.Printf("결과: %d\n", calculator.Add(a, b))
    case "-":
        fmt.Printf("결과: %d\n", calculator.Subtract(a, b))
    case "*":
        fmt.Printf("결과: %d\n", calculator.Multiply(a, b))
    case "/":
        result, err := calculator.Divide(a, b)
        if err != nil {
            fmt.Printf("오류: %v\n", err)
        } else {
            fmt.Printf("결과: %.2f\n", result)
        }
    default:
        fmt.Println("잘못된 연산자입니다.")
    }
}