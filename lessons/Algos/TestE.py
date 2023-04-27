import sys
n = int(sys.stdin.readline())
firsts = list(map(int, sys.stdin.readline().split(' ')))
count = 1
lowers = [0] * n
result = [1]
i = n - 1
for elem in firsts:
    lowers[elem - 1] = 1
    while i >= 0:
        if lowers[i] == 0:
            count += 1
            result.append(count)
            break
        else:
            i -= 1
            count -= 1
result.append(1)

print(' '.join(map(str, result)))

