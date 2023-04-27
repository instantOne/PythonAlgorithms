n = int(input())
a = [1, 2]
if n == 1:
    print("1")
elif n == 2:
    print("1 2")
else:
    for i in range(3, n + 1):
        a.append(i)
        a[(len(a) - 1) // 2], a[-1] = a[-1], a[(len(a) - 1) // 2]
    print(' '.join(map(str, a)))

    from collections import deque

    n = int(input())

    a1 = deque()
    a2 = deque()
    for i in range(n):
        operation = input().split(' ')

    for i in range(n):
        if operation[0] == '+':
            a2.append(operation[1])

        elif operation[0] == '*':
            a2.appendleft(operation[1])

        else:
            print(a1.popleft())

        if len(a1) < len(a2):
            a1.append(a2.popleft())
