"""
Find the given character position in the A - Z
"""

# Create an alphabets map string for getting the position of the given alphabet
alphabets = "abcdefghijklmnopqrstuvwxyz"

def get_char_pos (char):
    # Calculate the position of the character in the A - Z.
    # NOTE:
    # Compare with the lower case character as our mapping string is in lower case
    # Our mapping string is indexed from 0 to (n-1)
    return alphabets.find(char.lower()) + 1

# Get the input from the user
pos = get_char_pos(input("Enter any alphabet\n"))
print("Alphabet position is " + str(pos))