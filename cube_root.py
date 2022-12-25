"""
Check whether the given number is a perfect cube or not
"""

def check_is_cube (number):
    """
    Check whether the given number is a perfect cube or not
    Search for the number, can be done using binary search
    Start with the second half

    Args:
        number (int): number to check is cube or not_summary_

    Returns:
        bool: True  - the number is perfect cube
              False - the number is not a perfect cube
    """
    result = False
    end    = number
    start  = number >> 1
    cube = 0;

    while (start < end):
        # Check if we are at the number
        cube = start ** 3
        if cube == number:
            result = True
            break
        elif cube > number:
            end = start
            start >>= 1
        else:
            start += 1

    return result

# Get the number from the user
number = int(input("Enter the number\n"))
is_cube = check_is_cube(number)

if is_cube == True:
    print("The number is a perfect cube")
else:
    print("The number is not a perfect cube")