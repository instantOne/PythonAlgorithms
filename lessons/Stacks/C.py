from collections import deque
n = int(input())
trains = deque(list(map(int, input().split())))
first = deque()
second = deque()
minimum = min(trains)
flag = False
result = []
key = 0
for i in range(len(trains)):
    count = 0
    countsecond = 0
    if trains[i] == minimum:
        for j in range(key,i + 1):
            first.append(trains[j])
            count += 1
        result.append([1, count])
        key = j + 1
        for j in range(len(first) - 1, -1, -1):
            if first[j] == minimum:
                minimum += 1
                countsecond += 1
                second.append(first.pop())
            else:
                break
        result.append([2, countsecond])
if len(first) > 0:
    if list(sorted(first, reverse=True)) == list(first):
        result.append([2, len(first)])
        print(len(result))
        for i in range(len(result)):
            print(' '.join(map(str, result[i])))
    else:
        print(0)
else:
    print(len(result))
    for i in range(len(result)):
        print(' '.join(map(str, result[i])))



