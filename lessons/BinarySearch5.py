nums = list(map(int, input().split()))

def function(x):
    return nums[0] * x ** 3 + nums[1] * x ** 2 + nums[2] * x + nums[3]

right = 5.0
while function(right) * function(-right) >= 0:
    right *= 2
left = -right

while left + 0.00001 < right:
    x = (left + right) / 2
    if function(x) * function(right) <= 0:
        left = x
    else:
        right = x
print(left)