def add(num1,num2):
    return num1 + num2
def multiply(num1,num2):
    return num1 * num2
def subtract(num1,num2):
    return num1 - num2
def divide(num1,num2):
    return num1/num2
operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))
for symbol in operations:
    print(symbol)
operation_symbol = input("Choose an operation above:")
result = operations[operation_symbol](num1,num2)
print(f"{num1} {operation_symbol} {num2} = {result}")