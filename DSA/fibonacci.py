import sys
def fibonacci(n):
    fib_sequence = [0,1]
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        num1 , num2 = 0 , 1
        for i in range(n):
            num3 = num2 + num1
            fib_sequence.append(num3)
            num1 = num2
            num2 = num3
    return fib_sequence
n = int(sys.argv[1])
print(fibonacci(n))