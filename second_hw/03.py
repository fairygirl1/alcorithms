# найти количество уникальных путей

class Solution:
  def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
  # нахожу размеры
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    
    # создаю массив для хранения уникальных путей до каждой ячейки
    dp = [[0] * (n + 1) for i in range(m + 1)]
    dp[0][1] = 1  # из начальной точки можно пойти только вправо или вниз
# прохожусь по всем ячейкам
    for i in range(1, m + 1):
      for j in range(1, n + 1):
        if obstacleGrid[i - 1][j - 1] == 0: # если не препятствие
          dp[i][j] = dp[i - 1][j] + dp[i][j - 1] #  количество уникальных путей до ячейки равно сумме количества уникальных путей до ячейки сверху и слева 

    return dp[m][n] # количество путей до последней ячейки


#O(n)
