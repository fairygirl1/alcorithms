#Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
#O(n)

'''иду по каждому элементу матрицы слева направо и сверху вниз, если 1, 
то ответ увеличиваю на 1 и проверяю рядом стоящие элементы (предыдущие, в левую диагональ), если они 
все == 1, то этот элемент и тотал увеличиваю на минимальное значение рядом стоящих

'''

matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
def countSquares(matrix: list[list[int]]) -> int:
  total = 0
  min_value = matrix[0][0]
  #string
  for i in range(len(matrix)):
    #column
    for j in range(len(matrix[0])):
      #square of 1 element
      if matrix[i][j] == 1:
        total += 1
        if i>0 and j>0 and matrix[i-1][j] >0 and matrix[i][j-1] >0 and matrix[i-1][j-1] > 0:
          min_value = min(int(matrix[i-1][j]), int(matrix[i][j-1]), int(matrix[i-1][j-1]))
          matrix[i][j] = min_value + int(matrix[i][j]) 
          total += min_value

  return total
  
print(countSquares(matrix))