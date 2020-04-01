graph  = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F':[]
}

visited = []

def dfs(visited, graph, node) -> []:
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
    return visited

# Driver code
print(dfs(visited, graph, 'A')) 