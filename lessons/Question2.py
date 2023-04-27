import math

def read_array(n):
    array = []
    for i in range(n):
        array.append(int(input()))
    return array

def linear_search(array, value):
    for i in array:
        if i == value:
            return True
    return False

def binary_search(array, value):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == value:
            return True
        elif array[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return False

n = int(input("Enter the size of the array: "))
array = read_array(n)
array.sort()
q = int(input("Enter the number of queries: "))

for i in range(q):
    value = int(input("Enter the value to search for: "))
    if q <= n/math.log2(n):
        result = linear_search(array, value)
    else:
        result = binary_search(array, value)
    print("Value found:", result)
