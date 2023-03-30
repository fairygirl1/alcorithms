# 463. Island Perimeter
# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there 
# is exactly one island (i.e., one or more connected land cells).
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. 
# One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

# Прохожу горизонтально по матрице, если встречаю 1 - увеличиваю счетчик островов, 
# с каждой следующей прилегающей 1 - увеличиваю счетчик соседей.
# Возвращаю "кол-во островов*4 - кол-во соседей*2"

class Solution:
  def islandPerimeter(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    islands, neighbors = 0, 0

    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1:
          islands += 1
          if i + 1 < m and grid[i + 1][j] == 1:
            neighbors += 1
          if j + 1 < n and grid[i][j + 1] == 1:
            neighbors += 1

    return islands * 4 - neighbors * 2


# O(n)