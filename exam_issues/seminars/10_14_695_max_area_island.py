"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

https://leetcode.com/problems/max-area-of-island/

"""
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0
        count = 0
        seen = set()
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1 and (x, y) not in seen:
                    count += 1
                    start_point = (x, y)
                    stack = [start_point]
                    seen.add(start_point)
                    area = 0
                    while stack:
                        row, col = stack.pop()
                        area += 1
                        for x, y in (row-1, col), (row+1, col), (row, col-1), (row, col+1):
                            if (0 <= x <= len(grid)-1) and (0 <= y <= len(grid[0])-1) and grid[x][y] and ((x, y) not in seen):
                                stack.append((x, y))
                                seen.add((x, y))
                    max_area = max(max_area, area)
        print(count)
        return max_area

solution = Solution()
print(solution.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))