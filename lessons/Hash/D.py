s = input()
def manacher_even(s):
    n = len(s)
    even = [0] * n
    l, r = -1, -1
    for i in range(n - 1):
        if i < r:
            even[i] = min(r - i, even[l + r - i - 1])
        while i - even[i] >= 0 and i + even[i] + 1 < n and s[i - even[i]] == s[i + even[i] + 1]:
            even[i] += 1
        if i + even[i] > r:
            l, r = i - even[i] + 1, i + even[i]
    return sum(even)
def manacher_odd(s):
    n = len(s)
    odd = [1] * n
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            odd[i] = min(r - i + 1, odd[l + r - i])
        while i - odd[i] >= 0 and i + odd[i] < n and s[i - odd[i]] == s[i + odd[i]]:
            odd[i] += 1
        if i + odd[i] - 1 > r:
            l, r = i - odd[i] + 1, i + odd[i] - 1
    return sum(odd)
print(manacher_odd(s) + manacher_even(s))
