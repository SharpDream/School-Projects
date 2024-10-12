while True:
    num1 = float(input("Enter the first number: "))
    operation = input("Enter operation (+, -, *, /, %): ")

    if operation == '%':
        print(f"{num1}% = {num1 / 100}")
    else:
        num2 = float(input("Enter the second number: "))
        if operation == '+':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif operation == '-':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif operation == '*':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif operation == '/':
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Error! Division by zero.")
        else:
            print("Invalid operation")
