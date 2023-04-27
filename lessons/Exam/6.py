n, s = map(int, input().split())

# создание списка средних баллов и сортировка его по возрастанию
a = []
for i in range(n):
    l, r = map(int, input().split())
    a.append((l + r) // 2)
a.sort()

# бинарный поиск по ответу
l, r = 1, max(a)
ans = l
while l <= r:
    mid = (l + r) // 2
    # проверка возможности достижения медианного балла mid
    s1 = sum(a[:(n+1)//2])
    s2 = sum(b for b in a if b < mid)[:min((n+1)//2, len(a))]
    if s1 + s2 <= s:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)




