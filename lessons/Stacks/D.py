from collections import deque

n = int(input())

a1 = deque()
a2 = deque()
for i in range(n):

    op_and_num = input().split()

    if op_and_num[0] == '+':
        a2.append(op_and_num[1])

    elif op_and_num[0] == '*':
        a2.appendleft(op_and_num[1])

    else:
        print(a1.popleft())

    if len(a1) < len(a2):
        a1.append(a2.popleft())