"""
Find all the missing numbers in an array
"""

# Get the number of elements
max_ele = int(input("Enter the number of elements\n"))

# Get each elements one by one
arr = []
for index in range(max_ele):
    arr.append(int(input()))

"""
Print all the missing numbers in the given array
Run through each elements and check if is the consecutive number for the previous element
If not, print the missing number[s]

Args:
    arr     (list): array list
    max_ele (int) : max number of elements in the array
"""
num = arr[0]
index = 0
while index < max_ele:
    if num != arr[index]:
        print(num)
        num += 1
    else:
        index += 1
        num   += 1