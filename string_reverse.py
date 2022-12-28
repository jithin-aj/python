"""
Print the string in the reverse without using reverse
"""

# Get the input string from the user
string = input("Enter any string\n")

# Run through all the character and insert the character to the first position every time.
out_str = ""
for ch in string:
    out_str = ch + out_str # append with the previous string

print(out_str)