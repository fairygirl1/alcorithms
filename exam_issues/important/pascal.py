def generate(numRows):
    result=[]
    for i in range(numRows):
        if i >= 2: result.append([1]+[result[-1][x]+result[-1][x+1] for x in range(len(result[-1])-1)]+[1])
        else: result.append([1 for _ in range(i+1)])
    return result
for x in generate(5): print(x)