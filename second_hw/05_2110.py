'''
You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.

A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.

Return the number of smooth descent periods.
'''

prices = [3,2,1,4]
def getDescentPeriods(prices) -> int:
    n = len(prices)
    dp = [1]*n #массив из 1
    for i in range(1, n):
        if prices[i]+1 == prices[i-1]: #если цена в текущий день + 1 = цене в предыдущий день, 
        #то это мягкий спад (разница должна быть в 1)
            dp[i]=dp[i-1]+1 #предыдущий элемент + 1 период спада, если условие выполняется, 
            # првый элемент не трогаем

    return sum(dp)

print(getDescentPeriods(prices))



