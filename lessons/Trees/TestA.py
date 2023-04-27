class TreeStruct:
    def __init__(self):
        self.S = []
        self.flag = False
        self.x = 0

    def next(self, n):
        min = -1
        flag_min = False
        for i in range(len(self.S)):
            if (flag_min == False) and (self.S[i] >= n):
                min = self.S[i]
                flag_min = True
            elif (self.S[i] <= min) and (self.S[i] >= n):
                min = self.S[i]
        self.flag = True
        self.x = min
        print(min)

    def add(self, n):
        if (self.flag == True):
            self.S.append((n + self.x) % (10 ** 9))
            self.flag = False
        else:
            self.S.append(n)


A = TreeStruct()
amount = int(input())
for i in range(amount):
    operation, num = input().split()
    num = int(num)
    if operation == '+':
        A.add(num)
    else:
        A.next(num)
