def dfs():


with open('input.txt','r') as f:
    d = {}
    ans = []
    for _ in range(int(f.readline())):
        line = f.readline().split()
        for i in 0,1: d[line[i]] = [line[i-1]] if line[i] not in d else d[line[i]] + [line[i-1]]
    for _ in range(int(f.readline())):
        dest = f.readline().split()[0]
        # print(dest)
        line = f.readline().split()
        # print(line)
        res = []
        for source in line:
            
        ans.append(res)

for item in ans:
    print(len(item), ' '.join(item))

print(d)