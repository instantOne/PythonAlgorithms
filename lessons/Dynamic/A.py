n = int(input())
costs = list(map(int, input().split()))
if n > 2:
    for i in range(2, n - 1):
        costs[i] += min(costs[i - 1], costs[i - 2])
    print(min(costs[n - 2], costs[n - 3]) + costs[-1])
elif n == 2:
    print(costs[1])
else:
    print(costs[0])