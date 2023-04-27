s = input()
t = input()

n, m = len(s), len(t)
p = 31
mod = 10**9 + 9

p_pow = [1]
for i in range(1, max(n, m)):
    p_pow.append((p_pow[-1] * p) % mod)

h_s = [0]
for i in range(n):
    h_s.append((h_s[-1] + (ord(s[i]) - ord('a') + 1) * p_pow[i]) % mod)

h_t = 0
for i in range(m):
    h_t = (h_t + (ord(t[i]) - ord('a') + 1) * p_pow[i]) % mod

result = []
for i in range(n - m + 1):

    h = (h_s[i + m] - h_s[i] + mod) % mod
    if h == h_t * p_pow[i] % mod:
        result.append(i)

print(*result)
