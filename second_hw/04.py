class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    sell = 0 #максимальная прибыль, которую можно получить на текущий момент
    hold = -math.inf # максимальная потеря, которую можно понести на текущий момент (отрицательная бесконечность)

# иду по массиву цен на акции
    for price in prices:
    # сравниваю два элемента 
      sell = max(sell, hold + price)
      hold = max(hold, sell - price)

    return sell

   #O(n)
