def dfs(matrix, start_point):
    stack = [start_point]
    seen = {start_point}
    while stack:
        cur_vertex = stack.pop()
        # some actions
        for neig, edge in enumerate(matrix[cur_vertex]):
            if edge == 1 and neig not in seen:
                seen.add(neig)
                stack.append(neig)
    return seen

def is_connected(matrix): return len(dfs(matrix, 0)) == len(matrix)

def connectivity_components(matrix):
    ans = []
    seen = set()
    for i in range(len(matrix)):
        if i not in seen:
            component = dfs(matrix, i)
            ans.append(component)
            seen |= component
    print(seen)
    return ans

matrix = [
    [0,1,0,0,0,0],
    [1,0,1,1,0,0],
    [0,1,0,1,0,0],
    [0,1,1,0,0,0],
    [0,0,0,0,0,1],
    [0,0,0,0,1,0]
]
print(connectivity_components(matrix))