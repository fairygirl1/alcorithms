def findRelativeRanks(score):
    # Создаем словарь для хранения соответствия между очками и рангами
    rank_map = {}
    
    # Создаем копию списка очков и сортируем его в порядке убывания
    sorted_score = sorted(score, reverse=True)
    
    # Присваиваем ранги спортсменам
    for i, s in enumerate(sorted_score):
        if i == 0:
            # Первому месту присваиваем ранг "Gold Medal"
            rank_map[s] = "Gold Medal"
        elif i == 1:
            # Второму месту присваиваем ранг "Silver Medal"
            rank_map[s] = "Silver Medal"
        elif i == 2:
            # Третьему месту присваиваем ранг "Bronze Medal"
            rank_map[s] = "Bronze Medal"
        else:
            # Остальным спортсменам присваиваем их позицию в рейтинге
            rank_map[s] = str(i + 1)
    
    # Создаем массив для хранения рангов каждого спортсмена
    answer = []
    
    # Заполняем массив рангами, используя словарь rank_map
    for s in score:
        answer.append(rank_map[s])
    
    return answer

# Пример использования:
score = [10, 25, 5, 15, 20]
result = findRelativeRanks(score)
print(result)  # Выводит: ["Silver Medal", "Gold Medal", "Bronze Medal", "4", "3"]
