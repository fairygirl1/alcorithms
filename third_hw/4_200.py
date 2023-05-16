# 200. Number of Islands
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Решается поиском в глубину - прохожу по матрице построчно, когда встречаю единичку, 
# увеличиваю счетчик и дальше проверяю наличие единичек во всех направлениях.

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

def numIslands(grid) -> int:
        if not grid: return 0
        row = len(grid)
        col = len(grid[0])
        visited = set()
        count = 0
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        def findIsland(x,y):
            for dx, dy in directions:
                nx,ny = x+dx, y+dy
                if 0<=nx<row and 0<=ny<col and grid[nx][ny]=='1' and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    findIsland(nx,ny)
            
        for x in range(row):
            for y in range(col):
                if grid[x][y] == '1' and (x,y) not in visited:
                    count +=1
                    visited.add((x,y))
                    findIsland(x,y)         
        return count

print(numIslands(grid))
# O(n)