# arithmetic operations.py

def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"



# >>> python main.py
# Arithmetic Operations
# Enter the first number: 10
# Enter the second number: 2
# Enter the operation (add, subtract, multiply, divide): divide
# Result: 5.0
