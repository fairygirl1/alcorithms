class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
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
