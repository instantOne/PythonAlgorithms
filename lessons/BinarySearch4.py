import math
c = float(input())


left = 0
right = math.sqrt(c)
while left + 0.000001 < right:
    x = (left + right) / 2
    if x**2+math.sqrt(x+1) < c:
        left = x
    else:
        right = x
print(left)

# 5
# 3
# 7
# 02
# 05
# 050
# 051
# 005
# 049
# 000
# 50
# 51



