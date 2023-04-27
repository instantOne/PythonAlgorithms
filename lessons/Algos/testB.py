from itertools import permutations

def quicksort(nums, fst, lst):
    global count
    if fst >= lst: return

    i, j = fst, lst
    pivot = nums[(fst + lst) // 2]

    while i <= j:

        while nums[i] < pivot:
            count += 1
            i += 1
        count += 1
        while nums[j] > pivot:
            j -= 1
            count += 1
        count += 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
    quicksort(nums, fst, j)
    quicksort(nums, i, lst)
# a = [2, 4, 5, 1, 3]
# a = [5, 3, 1, 4, 2]
# a = [1, 4, 2, 3] 2 4 3 1
# a = 2 4 6 7 3 5 1
# a = 2 4 6 8 9 5 1 7 3
max = 0
n = int(input())
for perm in permutations(range(1, n+1)):
    perm = list(perm)
    copy = perm[:]
    count = 0
    quicksort(perm, 0, len(perm) - 1)
    if count >= max:
        max = count
        print(copy, count)
