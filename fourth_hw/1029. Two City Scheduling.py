"""
A company is planning to interview 2n people. 
Given the array costs where costs[i] = [aCosti, bCosti], 
the cost of flying the ith person to city a is aCosti, 
and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city 
such that exactly n people arrive in each city.

Жадный алгоритм
"""

def twoCitySchedCost(costs):
    total_cost = 0
    diff = [(a - b, i) for i, (a, b) in enumerate(costs)]  # Разница стоимостей между городами A и B, второй элемент индекс разницы в исходном списке
    # позволяет перебирать элементы списка costs 
    # вместе с их индексами, присваивая их значения 
    # переменным a и b на каждой итерации цикла.

    print(diff)
    diff.sort()  # Сортировка по возрастанию разницы
    print(diff)

    n = len(costs) // 2  # Количество людей для каждого города

    for i in range(n):
        total_cost += costs[diff[i][1]][0] #по индексам - diff[i][1] значит, что берем i сочетание разности и индекса в исходном списке, получаем индекс (элемент 1), потом вытаскиваем из списка costs стоимость перелета в город А   # Добавляем стоимость перелета в город A для первых n человек
# смотрим на отсортированные разницы стоимостей, первые n//2 - в город А, для этого проверяем индексы, чтобы взять правильную стоимость, аналогис=чно с людьми в город B, туда летят люди из второй части списка
    for i in range(n, len(costs)):
        total_cost += costs[diff[i][1]][1]  # Добавляем стоимость перелета в город B для остальных n человек

    return total_cost

costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]

print(twoCitySchedCost(costs))

# def twoCitySchedCost(self, costs: List[List[int]]) -> int:
#     diffs = []
#     for c1, c2 in costs:
#         diffs.append([c2-c1, c1, c2])
#     diffs.sort() #sorting by first value in the array
#     # [[-350, 400, 50], [-10, 30, 20], | [10, 10, 20], [170, 30, 200]]
#     res = 0
#     for i in range(len(diffs)):
#         if i < len(diffs)//2:
#             res += diffs[i][2] # third el of curr list in array
#         else:
#             res += diffs[i][1]
#     return res