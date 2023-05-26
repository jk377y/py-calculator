def calculator():
    # Welcome message and instructions
    print("Welcome to the calculator!")
    print("Enter two numbers and an operator to calculate the result.")

    # Get user input, convert to float which allows decimals and negative numbers as input
    num1 = float(input("Enter the first number: "))
    # Get operator input
    operator = input("Enter the operator (+, -, *, /): ")
    # Get user input, convert to float which allows decimals and negative numbers as input
    num2 = float(input("Enter the second number: "))

    # Calculate result based on operator, basic arithmetic operations
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        # If you're an idiot, you get an error message
        print("Invalid operator!")

    # Print result
    print("Result: ", result)

    # Ask user if they want to calculate another problem
    choice = input("Calculate another problem? (y/n): ")
    if choice.lower() == 'y':
        # If yes, run calculator() again
        calculator()
    else:
        # If no, print goodbye message
        print("Goodbye!")

# Run calculator() function
calculator()