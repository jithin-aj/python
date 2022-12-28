"""
Capitalise the first and last letter in the word if the character is vowel. Otherwise do nothing
"""

def is_vowel (char):
    """
    Check if the given letter is a vowel or not
    As we are checking this to capitalize the vowel letter in the word check for small case
    alphabets

    Args:
        char (str): alphabet

    Returns:
        bool: True- if the alphabet is a vowel. Else, False
    """
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        return True
    else:
        return False

def switch_case (word):
    """
    Check the first and last character of the word for vowels
    If the first or last character is a vowel, capitalize the character if not.

    Args:
        word (str): word to verify

    Returns:
        str: capitalized letters if so or the word as is
    """
    # Capitalize first letter if is vowel and is small case
    if is_vowel(word[0]):
        # Capitalize the first letter and append with the remaining letters as is
        copy = chr((ord(word[0]) - ord('a')) + ord('A')) + word[1:]

    # Proceed only if 2 or more character is present as there might be a case of single letter
    # between 2 words
    if len(word) < 2:
        return copy

    # Capitalize last letter is is vowel and is small case
    if is_vowel(word[-1]):
        copy = copy[:-1] + chr((ord(word[-1]) - ord('a')) + ord('A'))

    return copy

# Get the input string from the user
string = input("Enter any string\n")

# Reserve space to store the output
out_str = ""

# Run through all the words in the string
for word in string.split(' '):
    # Combine all the words and add space after each word
    out_str += switch_case(word) + " "

print(out_str)