"""
Program to find the difference between the array elements as below
arr[0] - arr[n-1], arr[1] - arr[n-2], ...
"""

def print_diff (arr, max_ele):
    print("\nDifference is:\n")
    for off in range(max_ele >> 1):
        print(arr[off] - arr[(max_ele - off) - 1])

# Get the array elements from the user
# First get the number of elements to store and then read the elements
arr = []
max_ele = int(input("Enter the number of elements\n"))
print("Enter array elements\n")

# Now read the elements one by one
for index in range(max_ele):
    arr.append(int(input()))

print_diff(arr, max_ele)
