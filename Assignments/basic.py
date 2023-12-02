import math
def add(num1, num2):
    return num1 + num2

def maximum(num1, num2):
    return max(num1, num2)

def factorial(num):
    if num < 0:
        return None
    fact = 1
    for i in range(1, num):
        fact += fact*i
    return fact

def simple_intrest(principle, rate, time):
    return (principle * rate * time) / 100

def compound_intrest(principle, rate, time, compunded = 1):
    return principle * (((1 + (rate/(100 * compunded))) ** (compunded * time)))

def check_armstrong(num):
    original_num = num
    new_num = 0
    while num != 0:
        digit = num % 10
        new_num += digit ** 3
        num //= 10
    return original_num == new_num

def area_of_circle(radius):
    return math.pi * radius * radius

def prime_numbers(start, end):
    for i in range(start, end + 1):
        is_prime = True
        for j in range(2, math.isqrt(i) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:  
            print(i, end=" ")

def check_prime(num):
    is_prime = True
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            is_prime = False
            break
    return is_prime

def nth_fibonacci(n):
    a , b = 0 , 1
    if n < 1:
        return "Plese give correct value"
    elif n == 1:
        return 0
    elif n < 4:
        return 1
    else:
        for _ in range(n - 2):
            c = a + b
            b , a = c , b
        return c

# def nth_multiple_fibonacci(n, num):

def to_ascii(char):
    if len(char) != 1:
        return "Please enter single character"
    return ord(char)

def sum_squares(n):
    sum = 0
    for i in range(n + 1):
        sum += (i ** 2)
    return sum

def sum_cubes(n):
    sum = 0
    for i in range(n + 1):
        sum += (i ** 3)
    return sum