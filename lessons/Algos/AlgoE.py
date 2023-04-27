n = int(input().strip())
firsts = list(map(int, input().strip().split()))
result = [1]
count = 1
a = [0] * n
last = n
for elem in firsts:
    if elem == last:
        count += 1
        a[elem - 1] = 1
        ones = 0
        for i in range(len(a) - 1, -1, -1):
            if a[i] == 1:
                ones += 1
            else:
                break
        count -= ones
        result.append(count)
        a = a[:len(a) - ones]
        last = len(a)
    else:
        a[elem - 1] = 1
        count += 1
        result.append(count)
print(' '.join(map(str, result)))












