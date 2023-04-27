def prefixFunction(s):
    n = len(s)
    prefix = [0] * n
    prefix[0] = 0

    for i in range(1, n):
        j = prefix[i-1]
        while j > 0 and s[i] != s[j]:
            j = prefix[j-1]
        if s[i] == s[j]:
            j += 1
        prefix[i] = j

    return prefix

def KMP(pattern, text):
    pSize = len(pattern)
    tSize = len(text)
    prefix = prefixFunction(pattern + "#" + text)
    res = []

    for i in range(pSize, pSize + 1 + tSize):
        if prefix[i] == pSize:
            res.append(i - pSize - 1)

    return res

if __name__ == '__main__':
    p = input().split()
    t = input().split()

    result = KMP(p, t)
    print(len(result))
    print(*result)
