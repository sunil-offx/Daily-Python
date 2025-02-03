def fibonacci_recursive(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example Usage
n = 10
fib_series = [fibonacci_recursive(i) for i in range(1, n+1)]
print("Fibonacci Sequence:", fib_series)
