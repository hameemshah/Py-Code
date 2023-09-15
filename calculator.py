def add(num1, num2):
    return num1 + num2

def multiply(num1, num2):
    return num1 * num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    else:
        return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def get_user_input(prompt):
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            print("Invalid input, please enter a number")
    return num

n1 = get_user_input("Enter the first number: ")
n2 = get_user_input("Enter the second number: ")

while True:
    print("Available operations:", ", ".join(operations.keys()))
    operation_symbol = input("Choose an operation above: ")
    if operation_symbol not in operations:
        print("Invalid operation symbol, Please try again")
    else:
        result = operations[operation_symbol](n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {result}")
        break
