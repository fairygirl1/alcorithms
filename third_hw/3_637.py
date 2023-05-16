# 637. Average of Levels in Binary Tree
# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

# Решается обходом в ширину с помощью очередей
# O(n)

from typing import List
from collections import deque

root = [3,9,20,0,0,15,7]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def averageOfLevels(root) -> List[float]:
    # Проверяем, что корневой узел существует
    if not root:
        return []
    
    # Инициализируем переменные для хранения результатов и очереди
    result = []
    queue = deque([root])

    while queue:
        # Получаем размер текущего уровня и сумму значений на этом уровне
        level_size = len(queue)
        level_sum = 0

        # Обрабатываем все узлы на текущем уровне
        for _ in range(level_size):
            # Извлекаем узел из очереди и обновляем сумму текущего уровня
            node = queue.popleft()
            level_sum += node.val

            # Если у узла есть левый потомок, добавляем его в очередь
            if node.left:
                queue.append(node.left)

            # Если у узла есть правый потомок, добавляем его в очередь
            if node.right:
                queue.append(node.right)

        # Вычисляем среднее значение на текущем уровне и добавляем его в результаты
        result.append(level_sum / level_size)

    # Возвращаем список средних значений по уровням дерева
    return result

print(averageOfLevels(root))