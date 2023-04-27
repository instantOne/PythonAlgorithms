from sys import stdin
#something
def topological_sort(edges, n):
    graph = [[] for _ in range(n)]
    visited = [False] * n
    order = []

    for b, e, w in edges:
        graph[b].append(e)

    def visit(v):
        if not visited[v]:
            visited[v] = True
            for neighbor in graph[v]:
                visit(neighbor)
            order.append(v)

    for v in range(n):
        visit(v)
    return order[::-1], visited

def bellman_ford(edges, order, s, t, n):
    dist = [float('inf')] * n
    dist[s] = 0

    for v in order:
        for b, e, w in edges:
            if b == v and dist[e] > dist[b] + w:
                dist[e] = dist[b] + w

    return dist[t]

n, m, s, t = map(int, stdin.readline().split())
edges = []
for _ in range(m):
    b, e, w = map(int, stdin.readline().split())
    edges.append((b - 1, e - 1, w))

order, visited = topological_sort(edges, n)

if not visited[t - 1]:
    print("Unreachable")
else:
    result = bellman_ford(edges, order, s - 1, t - 1, n)
    if result == float('inf'):
        print("Unreachable")
    else:
        print(result)
