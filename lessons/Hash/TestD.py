s = input()

s_length = len(s)

even = [0] * s_length
odd = [1] * s_length

#even
l, r = -1, -1
for i in range(s_length - 1):
    if i < r:
        even[i] = min(r - i, even[l + r - i - 1])
    while i - even[i] - 1 > 0 and i + even[i] + 1 < s_length and s[i - even[i]] == s[i + even[i] + 1]:
        even[i] += 1
    if i + even[i] > r:
        l = i - even[i] + 1
        r = i + even[i]
#odd
l, r = 0, 0
for i in range(1, s_length):
    if i < r:
        odd[i] = min(r - i + 1, odd[l + r - i])
    while i - odd[i] - 1 > 0 and i + odd[i] < s_length and s[i - odd[i]] == s[i + odd[i]]:
        odd[i] += 1
    if i + odd[i] - 1 > r:
        l = i - odd[i] + 1
        r = i + odd[i] - 1


print(odd)
print(even)
print(sum(odd + even))