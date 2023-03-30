#сложность алгоритма O(n), потому что программа будет повторяться по циклу while и n = количеству операций


#Given an integer num, return the number of steps to reduce it to zero.
#In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

num = 123
def steps (num):
    b = 0
    while num > 0: #повторение программы, пока переменная больше 0
        if num % 2 == 1:
            num -= 1
        else:
            num /= 2
        b += 1
    return b

print (steps(num))