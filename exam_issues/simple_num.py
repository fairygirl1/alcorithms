def simple(a):
    for delitel in range (2, 10):
        if a % delitel == 0:
            simple = False
        else:
            simple = True

    return simple

print(simple(5))