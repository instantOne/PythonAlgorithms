r = 0
l = 0
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
flag = False
while l < len(arr1):
    if arr1[l] == arr2[r]:
        flag = True
        break
    elif arr1[l] > arr2[r] and r + 1 < len(arr2):
        r += 1
    elif arr1[l] < arr2[r] and l + 1 < len(arr1):
        l += 1
    else:
        break

print(flag)