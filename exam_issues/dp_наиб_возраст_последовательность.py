def solution(arr):
    if len(arr) == 1:
        return 1
    
    res = [1]*len(arr)

    for i in range(1,len(arr)):
        for j in range(i):
            if arr[i]>arr[j] and res[i]<=res[j]:
                res[i] = res[j] + 1

    return max(res)

print(solution([5,2,3,7,1,0,9]))


