#https://neerc.ifmo.ru/wiki/index.php?title=Задача_о_расстоянии_Дамерау-Левенштейна
#ChatGPT prompt "Способы решения домерау левенштейна"
#ChatGPT prompt "Изначальные значения в матрице"
#https://habr.com/ru/post/676858/
s1 = input()
s2 = input()

matrix = [[0] * (len(s2) + 1) for j in range(len(s1) + 1)]


for i in range(len(s1) + 1):
    matrix[i][0] = i
for j in range(len(s2) + 1):
    matrix[0][j] = j

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            cost = 0
        else:
            cost = 1
        matrix[i][j] = min(
            matrix[i - 1][j] + 1,
            matrix[i][j - 1] + 1,
            matrix[i - 1][j - 1] + cost,
        )

        if i > 1 and j > 1 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]:
            matrix[i][j] = min(matrix[i][j], matrix[i - 2][j - 2] + cost)



print(matrix[-1][-1])
