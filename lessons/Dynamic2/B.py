import sys
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a)
current = []
result = []
def calculate(pos, s):
    global result
    global current
    if pos == m:
        if s * 2 == n:
            if not result or len(current) < len(result):
                result = list(current)
            return
        return
    calculate(pos + 1, s * 2)
    current.append(a[pos])
    calculate(pos + 1, s * 2 + a[pos])
    current.append(a[pos])
    calculate(pos + 1, s * 2 + a[pos] * 2)
    current = []
if s * 2 < n:
    print(-1)
else:
    calculate(0, 0)
    if not result:
        print(0)
    else:
        print(len(result))
        print(*result)
