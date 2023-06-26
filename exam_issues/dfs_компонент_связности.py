def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop() #возвращ последний элемент из стека
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            if vertex in graph:
                stack.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['E', 'G'],
    'G': ['F']
}

print(dfs(graph, 'A'))