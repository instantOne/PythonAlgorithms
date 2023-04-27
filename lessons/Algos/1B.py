r = 0
l = 0
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
mini = -1
minj = -1
mindif = 9999999
while l < len(arr1):
    if l == len(arr1) and r == len(arr2):
        break
    if abs(arr1[l] - arr2[r]) < mindif:
        mini = l
        minj = r
        mindif = abs(arr1[l] - arr2[r])
    if arr1[l] > arr2[r] and r + 1 < len(arr2):
        r += 1
    elif arr1[l] < arr2[r] and l + 1 < len(arr1):
        l += 1
    else:
        if l > r:
            r += 1
        else:
            l += 1


print(mini, minj, mindif)