"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 
for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
"""

def tribonacci(n):
    dp = [0] * (n + 3) # индексация от 3 (тк 0,1,2 уже заданы условием) и потом мы проверяем элементы вычитанием (а речь о сложении именно трех элементов, поэтому максимальный индекс при вычитании - 3), см 25 строка
    dp[0] = 0
    dp[1] = dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]

n = 5

print(tribonacci(n))