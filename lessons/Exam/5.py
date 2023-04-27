n = int(input())
a = list(map(int, input().split()))

sums_dict = {0: [-1]}
current_sum = 0
newa = []
count = 0

for i in range(n):
    current_sum += a[i]

    if current_sum in sums_dict:
        for index in sums_dict[current_sum]:
            newa.append((index + 1, i))

    if current_sum not in sums_dict:
        sums_dict[current_sum] = [i]
    else:
        sums_dict[current_sum].append(i)

for i in range(len(newa)):
    count += n - newa[i][1]
print(count)