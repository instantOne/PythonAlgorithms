from functools import cmp_to_key
from sys import stdin
def compare(a, b):

    x = a + b
    y = b + a

    if int(x) > int(y):
        return -1
    elif int(y) > int(x):
        return 1
    return 0

lines = [line.rstrip() for line in stdin]
print(''.join(map(str, sorted(lines, key=cmp_to_key(compare)))))
