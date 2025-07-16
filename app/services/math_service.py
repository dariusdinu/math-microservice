def calculate_pow(a: int, b: int) -> int:
    return a ** b

def calculate_fib(n: int) -> int:
    """Returns the n-th Fibonacci number (0-indexed)."""
    if n < 0:
        raise ValueError("Fibonacci input must be >= 0")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def calculate_factorial(n: int) -> int:
    """Returns factorial of n (n!)."""
    if n < 0:
        raise ValueError("Factorial input must be >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
