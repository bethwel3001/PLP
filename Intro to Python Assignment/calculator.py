def calculator():
    # Get the first number from the user
    num1 = input("Enter the first number: ")
    
    # Get the second number from the user
    num2 = input("Enter the second number: ")
    
    # Get the operation from the user
    operation = input("Enter the operation (+, -, *, /): ")
    
    try:
        # Convert inputs to float
        num1 = float(num1)
        num2 = float(num2)
        
    # Perform the operation based on user input (Had to research about this)
        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")

            # A number cannot be devided by 0, hence syntax Err
        elif operation == '/':
            if num1 == 0:
                print("syntax err")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("Err")
    except ValueError:
        print("Err")

# Call the calculator function
calculator()
