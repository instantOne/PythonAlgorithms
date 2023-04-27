import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
def dfs1(graph, visited, stack, vertex):
    visited[vertex] = True
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs1(graph, visited, stack, neighbor)
    stack.append(vertex)

def dfs2(graph, visited, components, vertex, current_component):
    visited[vertex] = True
    components[vertex] = current_component
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs2(graph, visited, components, neighbor, current_component)

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    graph_reversed = defaultdict(list)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph_reversed[b].append(a)

    visited = [False] * (n + 1)
    stack = []

    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(graph, visited, stack, i)

    visited = [False] * (n + 1)
    components = [0] * (n + 1)
    current_component = 0

    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            current_component += 1
            dfs2(graph_reversed, visited, components, vertex, current_component)

    print(current_component)
    print(*components[1:])

if __name__ == "__main__":
    main()
