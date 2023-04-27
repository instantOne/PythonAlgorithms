s = input()
m = int(input())

h = {0: 0}
p = [1]
k = 31
mod = 1000000009
maxn = 1000005
for i in range(1, maxn):
    p.append((p[i-1] * k) % mod)

for i in range(len(s)):
    h[i + 1] = ((h[i] + p[i] * ord(s[i])) % mod)
    #print(i)

def get_hash(l, r):
    #print(f"r+1:{r + 1} l:{l} h:{len(h)} p:{len(p)}")
    return (h[r + 1] - h[l]) * p[len(s) - l] % mod

for i in range(m):
    a, b, c, d = map(int, input().split())
    if get_hash(a - 1, b - 1) == get_hash(c - 1, d - 1):
        print("Yes")
    else:
        print("No")