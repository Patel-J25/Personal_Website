def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                return
        else:
            print("Invalid operator.")
            return
        
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")

# Run calculator
calculator()
