from math import INF as inf

def dijkstra(start, matrix):
    q = [start]
    visited = set()
    min_path = [inf] * len(matrix)
    min_path[start] = 0
    while q:
        cur_vertex = q.pop(0)
        visited.add(cur_vertex)

        for i, edge in enumerate(matrix[cur_vertex]):
            if edge:
                min_path[i] = min(min_path[cur_vertex] + edge, min_path[i])
                if i not in visited:
                    q.append(i)

    return min_path


def dfs(start, matrix):
    q = [start]
    seen = {start}
    while q:
        cur_vertex=q.pop()
        for i, edge in enumerate(matrix[cur_vertex]):
            if edge and (i not in seen):
                q.append(i)
                seen.add(i)
    return seen