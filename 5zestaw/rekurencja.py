def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fibonacci(n):
    a, b = 1, 1
    for i in range(0, n-1):
        a, b = b, a + b
    return a