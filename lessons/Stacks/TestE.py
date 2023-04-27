from collections import deque

n = int(input())
nums = list(map(int, input().split()))
multipliers = deque()
presumms = [0] * (n + 1)
result = 0

for i in range(n):
    presumms[i + 1] = presumms[i] + nums[i]

for i in range(n + 1):
    while multipliers and (i == n or nums[multipliers[-1]] > nums[i]):
        multiplier = multipliers.pop()
        if multipliers:
            left = multipliers[-1] + 1
        else:
            left = 0
        result = max(result, (presumms[i] - presumms[left]) * nums[multiplier])
    multipliers.append(i)

print(result)