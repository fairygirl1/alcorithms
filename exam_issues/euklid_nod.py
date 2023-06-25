# Нахождение наибольшего общего делителя с помощью алгоритма Евклида

def euklid(a, b):
    while b != 0:
        a, b = b, a%b
    return a
print(euklid(16, 28))
