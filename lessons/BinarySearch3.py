import sys

n = int(input())
left = 0
right = n + 1


def query(x):
    print(x)
    sys.stdout.flush()
    return input()


while left + 1 < right:
    c = (left + right) // 2
    response = query(c)
    if response == "<":
        right = c
    else:
        left = c
print(f"! {left}")
