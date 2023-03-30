#сначала нужно отсортировать данный список по порядку
#задаю переменную "разница" с плавающей точкой
#для каждого элемента в списке arr если разность между двумя соседними элементами меньше "разницы", вычисляем разницу
#если разность равна разнице, то дополняем список "ответ" с помощью аппенда
#возвращаем из функции список

#сложность O(n)



class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        difference = float('inf')
        for i in range(len(arr) - 1):
            if abs(arr[i + 1] - arr[i]) < difference:
                difference = abs(arr[i + 1] - arr[i])

        answer = []
        for i in range(len(arr) - 1):
            if abs(arr[i + 1] - arr[i]) == difference:
                answer.append((arr[i], arr[i + 1]))
        return answer

