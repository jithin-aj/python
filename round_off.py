"""
Round off the given number to the nearest round off value given
"""

def get_round_off (number, round_off):
    """
    Find where the number lies w.r.t given nearest value
    If the number is less than half of round_off value, round down to nearest value as it lies in
    lower half.
    If the number greater than half of round_off value, round up to nearest value as it lies in
    upper half

    Args:
        number (int)   : number need to round off
        round_off (int): nearest value to round off the number

    Returns:
        int: number after rounded off to the given nearest value
    """
    ret = (int((number + (round_off >> 1)) / round_off) * round_off)
    return ret

# Get the numbers from the user
number    = int(input("Enter the number\n"))
round_off = int(input("Enter the round off value\n"))

result = get_round_off(number, round_off)
print("Number " + str(number) + " is rounded to " + str(result))