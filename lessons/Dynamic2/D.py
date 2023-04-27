
#https://neerc.ifmo.ru/wiki/index.php?title=Нахождение_количества_разбиений_числа_на_слагаемые

result = []
n = int(input())

def dividing(x, position, max, num):
    if num == 0:
        result.append(' '.join(map(str, x[:position])))
    else:
        for i in range(1, min(num, max) + 1):
            x[position] = i
            dividing(x, position + 1, i, num - i)
x = [0] * 40
dividing(x, 0, n, n)

if n == 1:
    print(1)
else:
    for x in result:
        print(x)
