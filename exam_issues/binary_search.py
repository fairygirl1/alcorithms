def binary_search(a, arr):
    up = len(arr) - 1
    down = 0
    mid = (up + down) // 2

    while a != arr[mid]:
        if a > arr[mid]:
            down = mid +1
        elif a < arr[mid]:
            up = mid - 1
        mid = (up + down) // 2
    return mid
    
res = binary_search(20, [3,5,20,26,90,92,99])

print('Индекс искомого элемента ', res)