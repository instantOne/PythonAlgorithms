from collections import deque

n = int(input())
nums = list(map(int, input().split()))
result = 0
multipliers = deque()
presumms = [0] * (n + 1)
for i in range(len(nums)):
    if presumms:
        presumms[i] = presumms[i - 1] + nums[i]
    else:
        presumms = nums[i]

for i in range(len(nums)):
    while multipliers and nums[multipliers[-1]] > nums[i]:
        multiplier = multipliers.pop()
        if multipliers:
            left = multipliers[-1] + 1
        else:
            left = 0
        if left == 0:
            result = max(result, (presumms[i] - 0) * nums[multiplier])
        else:
            result = max(result, (presumms[i] - presumms[left]) * nums[multiplier])
    multipliers.append(i)

print(result)