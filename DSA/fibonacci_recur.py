import sys
def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# Example usage
n_terms = int(sys.argv[1])
result = fibonacci(n_terms)
print(f"Fibonacci sequence of {n_terms} terms: {result}")
