n = int(input())
b = sorted(input())
s = sorted(set(b))
begin = []
end = []
reserve = []

for i in range(len(s)):
    begin += s[i] * (b.count(s[i]) // 2)
    end += s[i] * (b.count(s[i]) // 2)
    if b.count(s[i]) % 2 != 0:
        reserve.append(s[i])

end.reverse()

if len(begin) == 0:
    print(reserve[0])
elif len(begin + end) % 2 == 0 and len(reserve) != 0:
    begin.append(reserve[0])
    print(''.join(map(str, begin + end)))
else:
    print(''.join(map(str, begin + end)))




