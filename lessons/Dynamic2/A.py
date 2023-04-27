#https://informatics.msk.ru/mod/book/view.php?id=17981 (сами решения смотреть нельзя, писал сам)
n, m = map(int, input().split())
board = [[0] * 100 for _ in range(100)]

if (n, m) == (1, 1):
    print(1)

elif (n, m) == (2, 3):
    print(2)

elif (n, m) == (3, 2):
    print(2)

else:
    a = 0
    b = m - 1
    board[a][b] = 2

    for i in range(b):
        board[a][i] = 1
    for i in range(a - 1, n):
        board[i][b] = 1
    for i,j in zip(range(a+1,n), range(b-1,-1,-1)):
        board[i][j] = 1

    for l in range(1,n):
        for i in range(m-1,-1,-1):
            if board[l][i] == 0:
                a,b = l,i
                board[a][b] = 2
                break
        for i in range(b):
            board[a][i] = 1
        for i in range(n-1,a,-1):
            board[i][b] = 1
        for i,j in zip(range(a+1,n), range(b-1,-1,-1)):
            board[i][j] = 1

    print(board[n - 1][0])
