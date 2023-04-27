import re

s = input().strip()
n = int(input())
matches = []
for i in range(n):
    matches.append(input().strip())

for i in range(n):
    result = [m.start() + 1 for m in re.finditer(f'(?={re.escape(matches[i])})', s)]
    print(f'{len(result)} {" ".join(map(str, result))}')
