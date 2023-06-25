def bubble_sort(arr):
    n = len(arr)
    for step in range(n):
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr

print(bubble_sort([4,3,6,2,8,1]))