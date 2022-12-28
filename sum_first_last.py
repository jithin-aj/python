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

    # Uncomment below for solving the above problem using step 1
    """
    # Using step1 as mentioned in above.
    # Convert the string input into integer
    num = int(number)

    # Get the last digit
    sum = num % 10

    # Run through each digits from the last until the first digit
    while num > 9:
        num /= 10

    sum += int(num)
    """

    # Solve using step2 as mentioned above
    # Convert the first and last character into int and find the sum.
    # sum = int(number[0]) + int(number[-1]) # comment this line to test step1

    return sum

# Get the number from the user
number = input("Enter the number\n")

# Get the sum of first and last digit in the given number
sum = sum_first_last(number)
print(sum)