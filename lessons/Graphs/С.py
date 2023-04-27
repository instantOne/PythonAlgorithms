from collections import deque

def is_valid_move(x, y, n):
    return 1 <= x <= n and 1 <= y <= n

def shortest_path(n, x1, y1, x2, y2):
    moves = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    visited = [[False for _ in range(n+1)] for _ in range(n+1)]
    queue = deque([(x1, y1, 0, [])])

    while queue:
        x, y, steps, path = queue.popleft()

        if (x, y) == (x2, y2):
            return steps, path + [(x, y)]

        if visited[x][y]:
            continue

        visited[x][y] = True

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny, n) and not visited[nx][ny]:
                queue.append((nx, ny, steps + 1, path + [(x, y)]))

    return -1, []

def main():
    n = int(input())
    for _ in range(2):
        if _ == 0:
            x1, y1 = map(int, input().split())
        elif _ == 1:
            x2, y2 = map(int, input().split())
    steps, path = shortest_path(n, x1, y1, x2, y2)

    print(steps)
    for x, y in path:
        print(x, y)

if __name__ == "__main__":
    main()
