n, m = map(int, input().split())

board = [[0 for j in range(m)] for i in range(n)]
if n >= 2 and m >= 3:
    board[1][2] = 1
if n >= 3 and m >= 2:
    board[2][1] = 1

def calculate_ways(i, j):
    if board[i][j] > 0:
        return board[i][j]

    if i - 1 >= 0 and j - 2 >= 0:
        board[i][j] += calculate_ways(i - 1, j - 2)
    if i + 1 < n and j - 2 >= 0:
        board[i][j] += calculate_ways(i + 1, j - 2)

    if i - 2 >= 0 and j - 1 >= 0:
        board[i][j] += calculate_ways(i - 2, j - 1)
    if i - 2 >= 0 and j + 1 < m:
        board[i][j] += calculate_ways(i - 2, j + 1)

    return board[i][j]

print(calculate_ways(n - 1, m - 1))