nums = list(map(int, input().split()))
arr = list(map(int, input().split()))
questions = list(map(int, input().split()))

def bin_search(num):
    left = -1
    right = len(arr) - 1
    while left + 1 < right:
        c = (left + right) // 2
        if arr[c] < num:
            left = c
        else:
            right = c
    if arr[right] == num:
        print("YES")
    else:
        print("NO")

for num in questions:
    bin_search(num)
