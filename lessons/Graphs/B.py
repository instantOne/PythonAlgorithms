def dfs(v, graph, visited, in_stack):
    visited[v] = True
    in_stack[v] = True

    for neighbor in graph[v]:
        if not visited[neighbor]:
            if dfs(neighbor, graph, visited, in_stack):
                return True
        elif in_stack[neighbor]:
            return True

    in_stack[v] = False
    return False


def has_cycle(n, graph):
    visited = [False] * (n + 1)
    in_stack = [False] * (n + 1)

    for v in range(1, n + 1):
        if not visited[v]:
            if dfs(v, graph, visited, in_stack):
                return True

    return False


def main():
    n, m = map(int, input().split())
    graph = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    print(int(has_cycle(n, graph)))


if __name__ == "__main__":
    main()
