"""
Check whether the given number is a perfect square
"""

def check_is_square (number):
    """
    Check whether the given number is a perfect square or not
    Search for the number, can be done using binary search
    Start with the second half

    Args:
        number (int): number to check is square or not
    """
    result = False
    end    = number
    start  = number >> 1
    square = 0;

    while (start < end):
        # Check if we are at the number
        square = start ** 2
        if square == number:
            result = True
            break
        elif square > number:
            end = start
            start >>= 1
        else:
            start += 1

    return result

# Get the number from the user
number = int(input("Enter the number\n"))
is_square = check_is_square(number)

if is_square == True:
    print("The number is a perfect square")
else:
    print("The number is not a perfect square")