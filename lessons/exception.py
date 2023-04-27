a = int(input())
b = int(input())
try:
    result = int(a / b)
    print(result)
except ZeroDivisionError:
    print("На ноль делить нельзя")

