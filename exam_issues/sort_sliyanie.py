'''
Сортировка слиянием работает по принципу разделяй и властвуй:
большой массив рекурсивно делится на маленькие подмассивы длины 1

далее для них вызывается функция слияния, в которой определяется 
пустой список для записи результатов
пока списки не закончатся, сравниваются элементы двух списков

в конце методом .extend список дополняется отсортированными элементами
другой половинки (для случая, когда одна половинка закончилась, а в другой 
еще есть элементы)

этот список возвращается из функции слияния и выводится на печать
'''

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    res = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            res.append(left[left_idx])
            left_idx += 1

        else:
            res.append(right[right_idx])
            right_idx += 1

        res.extend(left[left_idx:])
        res.extend(right[right_idx:])

        return res
    
print(merge_sort([7,5,4,9,0,1,8,4]))