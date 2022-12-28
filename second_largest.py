"""
Find the second largest element in an array without using any methods
"""

def get_second_largest (arr, max_ele):
    """
    Find the second largest element in an array
    Consider the first element as first and second largest element and compare the remaining
    elements with the first and second largest number

    Args:
        arr (list): array list
        max_ele (int): max elements in the list

    Returns:
        int: second largest element in an array
    """
    largest = second_largest = arr[0]
    for ele in range(max_ele):
        if arr[ele] > largest:
            second_largest = largest
            largest        = arr[ele]
        elif arr[ele] > second_largest and arr[ele] != largest:
            second_largest = arr[ele]

    return second_largest


# Get the number of elements
max_ele = int(input("Enter the number of elements\n"))

# Get each elements one by one
arr = []
for index in range(max_ele):
    arr.append(int(input()))

second_largest = get_second_largest(arr, max_ele)
print(second_largest)