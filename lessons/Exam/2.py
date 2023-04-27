import math
juniors, seniors, amount = tuple(map(int, input().split()))
print(math.ceil(juniors * amount / seniors))