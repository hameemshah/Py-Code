memo = {}

def nth_fibonacci(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = nth_fibonacci(n - 1) + nth_fibonacci(n - 2)
    return memo