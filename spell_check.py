"""
Basic spell check program which checks the complete sentence and check for the individual letter 'a'
and if the next occurring word is a vowel then replace it with "an"
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


def spell_check(string):
    """
    Go through all the words one after the other, instead of character character.
    Split the string into words, check for individual word 'a'
    If found 'a', check if the next occurring word starts with vowel, correct 'a' to "an" if so.
    If not found 'a' do nothing.

    Args:
        string (str): user input string
    """
    global out_str

    # Run through all the words in the string and check for word 'a'
    # Split the string into list for lesser iterations
    str_split = string.split(' ')
    for word in range (len(str_split)):
        # Check if the next occurring word is 'a'
        if str_split[word] == 'a':
            # Check if the next occurring word starts with a vowel or not
            word += 1
            if is_vowel(str_split[word][0]):
                # Correct 'a' to 'an'
                out_str += "an "
            else:
                # Copy as is
                out_str += str_split[word] + ' '
        else:
            out_str += str_split[word] + ' '


# Get the input string from the user
string = input("Enter any string\n")

# Reserve for storing the resultant new string
out_str = ""
spell_check(string)

print(out_str)