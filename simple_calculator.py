"""
A simple calculator program where we get the operands and operation from the user and perform the
desired calculation
"""

def calculator (op):
    """Perform a simple arithmetic operation

    Args:
        op (str):
        op[0]: operand 1
        op[1]: operator to perform
        op[2]: operand 2

    Returns:
        int: result of the requested operation
    """
    # Get the operands and operator
    operand_1 = int(op[0])
    operator  = op[1]
    operand_2 = int(op[2])

    # Perform calculation
    if operator == '+':
        return operand_1 + operand_2
    elif operator == '-':
        return operand_1 - operand_2
    elif operator == '*':
        return operand_1 * operand_2
    elif operator == '/':
        return operand_1 / operand_2
    else:
        print("Invalid operator")
        exit()

# Get the inputs from the user
# Format: <operand_1> <operator> <operand_2>
calculation = input("Enter the operands and operation to perform as given below\n\
operand_1 operator operand_2\n")

# Perform operation and print the result
result = calculator(calculation.split())
print("The result is " + str(result))