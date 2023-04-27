from collections import deque

n, k = map(int, input().split())
sequence = list(map(int, input().split()))

window = deque()
result = []

for i, x in enumerate(sequence):
    while len(window) > 0 and sequence[window[-1]] > x:
        window.pop()
    window.append(i)

    if window[0] == i - k:
        window.popleft()

    if i >= k - 1:
        result.append(sequence[window[0]])

print(*result)
