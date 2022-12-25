"""
Given RGB(Red, Green, Blue) value in 2 bytes long where R, G & B are packed in 2 bytes each having
respective bit length which is given by the user input.
Extract individual value of R, G & B
"""

def unzip_rgb (rgb, r, g, b):
    """
    Extract RGB individual values
    Calculate the number of bits to mask and extract the individuals.
    The max value each can have is 0 to 2^n - 1, where n is the number of bits it holds

    Args:
        rgb (int) : 2 byte zipped value
        r (int)   : number of bits R holds
        g (int)   : number of bits G holds
        b (int)   : number of bits B holds_summary_

    Returns:
        int: extracted RGB value in 3 bytes
    """

    bits_in_byte = 8

    # Get blue first as it is placed at the end
    blue   = rgb & ((2 ** b) - 1)
    blue <<= bits_in_byte - b

    # Skip blue and move to green
    rgb   >>= b
    green   = rgb & ((2 ** g) - 1)
    green <<= bits_in_byte - g

    # Skip green and move to red
    rgb >>= g
    red   = rgb & ((2 ** r) - 1)
    red <<= bits_in_byte - r

    # Pack all the 3 individual bytes into 1
    ret = red;
    ret = (ret << bits_in_byte) | green
    ret = (ret << bits_in_byte) | blue

    return ret

# Get user input
rgb_2b = int(input("Enter the 2 byte RGB value\n"), 16)
r_bit  = int(input("Enter number of bit[s] Red holds\n"))
g_bit  = int(input("Enter number of bit[s] Green holds\n"))
b_bit  = int(input("Enter number of bit[s] Blue holds\n"))

# unzip the 2 byte value into 3 bytes
rgb_3b = unzip_rgb(rgb_2b, r_bit, g_bit, b_bit)
print(hex(rgb_3b))