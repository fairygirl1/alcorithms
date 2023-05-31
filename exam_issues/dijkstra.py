# алгоритм дейкстры используется для нахождения кратчайшего (самого дешевого пути) во
# взвешенном графе

import sys
from heapq import heappop, heappush

def dijkstra(graph, start):
    distances = {}  # Словарь для хранения кратчайших расстояний до вершин
    visited = set()  # Множество для отслеживания посещенных вершин
    heap = [(0, start)]  # Куча для выбора вершины с наименьшим расстоянием

    # Инициализация расстояний
    for vertex in graph:
        distances[vertex] = sys.maxsize
    distances[start] = 0

    while heap:
        current_distance, current_vertex = heappop(heap)  # возвращает наименьший элемент из кучи - вершину с наименьшим расстоянием

        # Проверяем, была ли вершина уже обработана
        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        # Обновляем расстояния до соседних вершин
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heappush(heap, (distance, neighbor)) #Добавляет элемент в кучу

    return distances

# Пример графа в виде словаря смежности с весами ребер
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'D': 2},
    'C': {'A': 3, 'D': 6},
    'D': {'B': 2, 'C': 6}
}

# Запуск алгоритма Дейкстры с начальной вершиной 'A'
distances = dijkstra(graph, 'A')

# Вывод кратчайших расстояний до всех вершин
for vertex, distance in distances.items():
    print(f"Shortest distance to vertex {vertex}: {distance}")
