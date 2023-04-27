n = list(map(int, input().split()))
increased = None
decreased = None
for i in range(3):
    if n[i] == n[i + 1]: pass
    elif n[i] < n[i + 1]: increased = True
    else: decreased = True
if increased and decreased:
    print("NO")
else:
    print("YES")