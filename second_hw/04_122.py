'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
'''
   #O(n)

prices = [7,1,5,3,6,4]
def maxProfit(prices) -> int:
  profit = 0
  for i in range(1, len(prices)):
    #скипаем 0 индекс, потому что для каждого элемента будем проверять предыдущий
    # если цена в текущий день больше, чем в предыдущий, можем получить профит, 
    # если купим в предыдущий день и сегодня продадим
    if prices[i] > prices[i-1]:
      profit += (prices[i] - prices[i-1])

  return profit

print(maxProfit(prices))