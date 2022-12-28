"""
Printing the permutations and combinations of a given word as shown below
Input : Space
Output: 'S' 'p' 'a' 'c' 'e' "Sp" "pa" "ac" "ce" "Spa" "pac" "ace" "Spac" "pace" "Space"
"""

def print_comb (str, length, comb):
    """
    Print all the possible combinations for the given number of character combination in the string

    Args:
        str    (str): string of characters
        length (int): number of characters
        comb   (int): number of character combination to print
    """
    for off in range(length):
        for ch in range(comb):
            print(str[ch + off])
        print(" ")

# Get the word from the user
string = input("Enter any string\n")

# Since we have a string, we need number of combinations that are possible like mentioned above
# From the example "Space", we can observe that we get number of permutations similar to number of
# character combination like 1char combinations 2char combinations and so on...
# So first run through every character combination
max_comb = len(string)
for comb in range (max_comb):
    print_comb(string, max_comb - comb, comb + 1)