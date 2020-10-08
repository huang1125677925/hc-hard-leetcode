n, m = map(int, raw_input().split())

res = []
listn = range(n)

def union(a, b):
    temp = min(a, b)
    while listn[temp] != temp:
        temp = listn[temp]
    listn[a] = temp
    listn[b] = temp
    
for i in range(m):
    temp = raw_input().split()
    if temp[0] == 'u':
        union(int(temp[1]), int(temp[2]))
    else:
        x, y = listn[int(temp[1])], listn[int(temp[2])]
        if x == y:
            res.append(1)
        else:
            res.append(0)
            
for item in res:
    print item
    
    