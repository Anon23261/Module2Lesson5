# Task 1: Create functions for each arithmetic operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use
def get_user_input():
    operation = input("Choose operation: add, subtract, multiply, divide: ").strip().lower()
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return operation, num1, num2

# Task 3: Ensure your code can handle division by zero and other potential errors
def calculator():
    operation, num1, num2 = get_user_input()
    
    if operation == "add":
        print("Result:", add(num1, num2))
    elif operation == "subtract":
        print("Result:", subtract(num1, num2))
    elif operation == "multiply":
        print("Result:", multiply(num1, num2))
    elif operation == "divide":
        print("Result:", divide(num1, num2))
    else:
        print("Error: Invalid operation")

calculator()
