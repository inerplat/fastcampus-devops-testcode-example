package org.example;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Calculator calculator = new Calculator();
        Scanner scanner = new Scanner(System.in);

        System.out.print("첫 번째 숫자: ");
        int a = scanner.nextInt();
        System.out.print("연산자 (+, -, *, /): ");
        char operator = scanner.next().charAt(0);
        System.out.print("두 번째 숫자: ");
        int b = scanner.nextInt();

        try {
            switch (operator) {
                case '+' -> System.out.println("결과: " + calculator.add(a, b));
                case '-' -> System.out.println("결과: " + calculator.subtract(a, b));
                case '*' -> System.out.println("결과: " + calculator.multiply(a, b));
                case '/' -> System.out.println("결과: " + calculator.divide(a, b));
                default -> System.out.println("잘못된 연산자입니다.");
            }
        } catch (IllegalArgumentException e) {
            System.out.println("오류: " + e.getMessage());
        }

        scanner.close();
    }
}