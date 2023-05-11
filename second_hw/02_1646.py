'''
You are given an integer n. A 0-indexed integer array nums of length n + 1 is generated in the following way:

nums[0] = 0
nums[1] = 1
nums[2 * i] = nums[i] when 2 <= 2 * i <= n
nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n

Return the maximum integer in the array nums​​​.
'''
#O(n)

def getMaximumGenerated(n: int) -> int:
    if n < 1:
        return 0
    elif n == 1:
        return 1
    arr = [0] * (n+1)
    
    arr[0] = 0 #condition
    arr[1] = 1 #condition
    
    for i in range(0, n + 1):
        # если индекс 2 * i, то nums[2 * i] получает значение nums[i]
        if 2 <= 2 * i <= n:
            arr[2 * i] = arr[i]
        
        # если индекс 2 * i + 1, то nums[2 * i + 1] получает значение nums[i] + nums[i + 1]
        if 2 <= 2 * i + 1 <= n:
            arr[2 * i + 1] = arr[i] + arr[i + 1]
    
    return max(arr)
    # возвращает максимальное значение в последовательности, которое соответствует максимальному элементу в списке nums.
    

print(getMaximumGenerated(7))
