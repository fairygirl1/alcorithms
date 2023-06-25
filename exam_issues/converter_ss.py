def converter(a, ss):
    res = []
    while a != 0:
        res.append(a%ss)
        a = a // ss
    res.reverse()
    res = ''.join(map(str, res))
    return res


print(converter(6, 2))