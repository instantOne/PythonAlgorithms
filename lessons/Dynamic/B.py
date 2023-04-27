n = int(input())

def count_stacks(n):
    if n == 1:
        return 3
    elif n == 2:
        return 8
    else:
        return 2 * count_stacks(n - 1) + count_stacks(n - 2) * 2
print(count_stacks(n))

# 2 --- 9 - 1 = 86
# 3 --- 27 - 5 = 22
# 4 --- 81 - 21 = 60
# 5 --- 243 - 79 = 164
# 6 --- 729 - 281 = 448
# 7 --- 2187 - 963 = 1224