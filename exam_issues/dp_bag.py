def bag(weights, values, capacity):
    n = len(weights)
    dp = [[0]*(capacity+1) for _ in range (n+1)] #будет содержать макс стоимость предметов
    
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            if weights[i-1]>j: #если вес предмета больше вместимости
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], values[i-1] + dp[i-1][j - weights[i-1]])

    res = dp[n][capacity]

    selected = []

    i = n
    j = capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i-1][j]:
            selected.append(i-1)
            j -= weights[i-1]
        i -= 1

    selected.reverse()

    return res, selected
        
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 7

result_value, result_items = bag(weights, values, capacity)
print("Максимальная суммарная стоимость:", result_value)
print("Выбранные предметы (индексы):", result_items)