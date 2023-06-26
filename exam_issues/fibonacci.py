def fibonacci(n):
    res = [0] * (n+1)

    res[0] = 0
    res[1] = res[2] = 1

    for i in range(3, n+1):
        res[i] = res[i-2] + res[i-1]

    return res[-1]

print(fibonacci(5))