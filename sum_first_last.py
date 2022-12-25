"""
Find the sum of first and last digit in the given number
"""

def sum_first_last (number):
    """
    Find the sum of first and last digit in the given number, this can be done in 2 ways
    1. convert the number into int and get first and last digit using % operator. This uses %
       operator which is a costly operator
    2. Since we know we get the input in string, the length of the string should give us the last
       digit which is enough to get the sum of first and last digit.

    Here we will be following the latter method

    Args:
        number (str): number from the user input

    Returns:
        int: sum of first and last digits
    """

    # The length of the string should give us the last digit
    # NOTE: Our index starts with 0
    last = len(number) - 1

    # Calculate the sum
    sum = int(number[0]) + int(number[last])
    return sum

# Get the number from the user
number = input("Enter the number\n")

# Get the sum of first and last digit in the given number
sum = sum_first_last(number)
print(sum)