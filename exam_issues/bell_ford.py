# алгоритм Беллмана-Форда используется для нахождения кратайшего 
# (самого дешевого пути) во
# взвешенном графе с ребрами с отрицательными весами

def bellman_ford(graph, start):
    # Инициализация расстояний до всех вершин как бесконечность
    distances = {vertex: float('inf') for vertex in graph}
    # Расстояние до начальной вершины равно 0
    distances[start] = 0

    # Проходим по всем ребрам графа |V| - 1 раз
    for _ in range(len(graph) - 1):
        # Проходим по всем ребрам и обновляем расстояния до соседних вершин
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                new_distance = distances[vertex] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    # Проверяем наличие отрицательных циклов
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            if distances[vertex] + weight < distances[neighbor]:
                # Обнаружен отрицательный цикл
                return None

    return distances

# Пример графа в виде словаря смежности с весами ребер
graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}

start_vertex = 'A'
distances = bellman_ford(graph, start_vertex)

if distances is None:
    print("Граф содержит отрицательный цикл")
else:
    for vertex, distance in distances.items():
        print(f"Кратчайшее расстояние от вершины {start_vertex} до вершины {vertex}: {distance}")