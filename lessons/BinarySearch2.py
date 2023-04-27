nums = list(map(int, input().split()))
arr = list(map(int, input().split()))
questions = list(map(int, input().split()))

def find_nearest(num):
    left = -1
    right = len(arr) - 1
    while left + 1 < right:
        c = (left + right) // 2
        if arr[c] < num:
            left = c
        else:
            right = c
    if abs(arr[right - 1] - num) <= abs(arr[right] - num) and arr[right] != num:
        print(arr[right - 1])
    else:
        print(arr[right])


for num in questions:
    find_nearest(num)