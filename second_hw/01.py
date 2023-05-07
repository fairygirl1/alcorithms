class Solution:
  def countSquares(self, matrix: list[list[int]]) -> int:
  # идем по каждой строке матрицы
    for i in range(len(matrix)):
    # теперь идем по столбцам
      for j in range(len(matrix[0])):
        if matrix[i][j] == 1 and i > 0 and j > 0:
        # если элемент = 1, то к нему прибавляется минимальное значение из левого, верхнего и диагонального элементов.
          matrix[i][j] += min(matrix[i - 1][j - 1],
                              matrix[i - 1][j], matrix[i][j - 1])
    return sum(sum(row) for row in matrix)
    # подсчитывает сумму всех элементов матрицы matrix и возвращает ее. генерирую список из сумм элементов в каждой строке, а потом общую сумму всех элементов матрицы


    #O(n)
