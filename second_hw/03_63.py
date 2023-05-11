# найти количество уникальных путей
'''
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.
'''

#O(n)
# 1 - по ним ходить нельзя, движение только вправо и вниз

obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]


def uniquePathsWithObstacles(obstacleGrid) -> int:
  m, n = len(obstacleGrid), len(obstacleGrid[0])
  dp = [[0] * (n + 1) for _ in range(m + 1)]
  #создаю двумерный массив из нулей
  # на один элемент больше, потому что буду проверять клетки по левой верхней диагонали, 
  # это чтобы программа не словамалась
  dp[0][1] = 1 #клетка старта, присвиваю этой строке 1
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if obstacleGrid[i - 1][j - 1] == 0: #если свободно, иду в эту клетку и проеряю, 
        # есть ли пути в летки по левой диагонали, записываю сумму (сумма уникальных путей в эту клетку
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]


  return dp[m][n]
      

print(uniquePathsWithObstacles(obstacleGrid))