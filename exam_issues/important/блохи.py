from math import inf





def kon(x,y):
    dx = [+1,+1,-1,-1,+2,-2,-2,+2]
    dy = [+2,-2,-2,+2,+1,+1,-1,-1]
    res = []
    for i in range(len(dx)):
        res.append((x+dx[i],y+dy[i]))
    return res


def gen_matrx(n,m,s,t):
    matrix = [[inf]*m for _ in range(n)]
    matrix[s-1][t-1] = 0
    queue = [(s-1,t-1)]
    seen = {(s-1,t-1)}
    while queue:
        x,y = queue.pop(0)
        neighbours = kon(x,y)
        for neig in neighbours:
            new_x, new_y = neig
            if 0 <= new_x < len(matrix) and 0<= new_y < len(matrix[0]):
                matrix[new_x][new_y] = min(matrix[new_x][new_y], matrix[x][y]+1)
                if neig not in seen:
                    seen.add(neig)
                    queue.append(neig)
    return matrix


with open('input.txt') as f: 
    n,m,s,t,q = map(int, f.readline().split())
    matrix = gen_matrx(n,m,s,t)
    res = -1
    for _ in range(q):
        x, y = map(int, f.readline().split())
        res = max(res, matrix[x-1][y-1])
    print(-1 if res == inf else res)

for row in matrix: print(*row)
        
