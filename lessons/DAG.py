n = int(input())
m = int(input())
ways = [False for x in range(m)]
count = 0
for i in range(m):
    a, b = map(int, input().split())
    ways[a - 1] = True

for i in range(m):
    if ways[i] == False:
        count += 1
if count == 0:
    print(count + 1)
else:
    print(coun )

# 5
# 4
# 2 3
# 3 4
# 4 5
# 1 5