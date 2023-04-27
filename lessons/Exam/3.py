n = int(input())
s = input()

count = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

left = 0
min_len = n + 1

for right in range(n):
    count[s[right]] += 1

    while all(count.values()):
        min_len = min(min_len, right - left + 1)
        count[s[left]] -= 1
        left += 1

    if right == n - 1 and not all(count.values()):
        break

if min_len == (n + 1):
    print("-1")
else:
    print(min_len)
