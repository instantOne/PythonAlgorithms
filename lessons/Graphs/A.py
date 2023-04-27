import sys
sys.setrecursionlimit(100000000)
def dfs(v, graph, visited, component):
    visited[v] = True
    component.append(v)
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, component)

def connected_components(n, edges):
    graph = {i: [] for i in range(1, n+1)}
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    visited = {i: False for i in range(1, n+1)}
    components = []
    for v in range(1, n+1):
        if not visited[v]:
            component = []
            dfs(v, graph, visited, component)
            components.append(sorted(component))

    return components

n, m = map(int, input().split())
edges = []
for i in range(m):
    edges.append(list(map(int, input().split())))

components = connected_components(n, edges)

print(len(components))
for component in components:
    print(len(component))
    print(' '.join(map(str, component)))
