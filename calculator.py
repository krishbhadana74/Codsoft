
def simple_calculator():
   
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("Select operation:")
    print(" + for Addition")
    print(" - for Subtraction")
    print(" * for Multiplication")
    print(" / for Division")
    
    operation = input("Enter operation symbol: ")
    

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation selected."
    
    return f"Result: {num1} {operation} {num2} = {result}"


simple_calculator()
