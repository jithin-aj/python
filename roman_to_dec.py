"""
Convert the roman numbers into decimal
"""
import re

def is_valid_exp(roman):
    """
    Validate the given Roman number and return is valid or not
    The below is the format for which the Roman number format should match
    The largest known Roman number is MMMCMXCIX (3999)
    So from the above number
    M - 1000 max-> MMM
    C - 100  max-> CCC/DCCC
    X - 10   max-> XXX/LXXX
    I - 1    max-> III/VIII
    So validate with the above consecutive representation of the number

    Args:
        roman (str): Roman number

    Returns:
        bool: True  - the Roman number is valid
              False - invalid format
    """
    return (bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", roman)))


def decimal (rn):
    """
    Convert the given Roman character to it's decimal equivalent

    Args:
        rn (str): Roman character

    Returns:
        int: decimal equivalent to the Roman character
    """
    if rn == 'I':
        return 1
    elif rn == 'V':
        return 5
    elif rn == 'X':
        return 10
    elif rn == 'L':
        return 50
    elif rn == 'C':
        return 100
    elif rn == 'D':
        return 500
    elif rn == 'M':
        return 1000
    else:
        # Invalid Roman character
        return -1

def roman_to_dec (roman):
    # Validate the input Roman format
    if is_valid_exp(roman) != True:
        return -1

    # Run through all the Roman characters
    # NOTE: Roman number is not continuos as Arabic numbers.
    # Ex: 5 in Roman is represented as IV
    #     9 in Roman is represented as IX and so on...
    # So we must also keep an eye on the next or previous occurring Roman character to know
    # whether we need to add or subtract with the current character.
    dec = 0
    cur_rn = decimal(roman[0])
    for rn in range(1, len(roman)):
        next_rn = decimal(roman[rn])

        if cur_rn < next_rn:
            dec -= cur_rn
        else:
            dec += cur_rn

        # Switch to next pair
        cur_rn = next_rn

    return dec + cur_rn

# Get the input Roman number in string
roman_num = input("Enter roman number\n")

# Get decimal equivalent to the Roman input
decimal = roman_to_dec(roman_num)
if decimal == -1:
    print("Invalid input!!!")
else:
    print(decimal)
