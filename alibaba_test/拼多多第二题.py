m, n = list(map(int, raw_input().split()))
data = []
for i in range(m):
    temp = map(int, raw_input().split())
    data.append(temp)
    
ress = []
def dfs(data, i, j, res, m, n, flag, flagnum):
    if data[i][j] == 1:
        res[0] += 1
        data[i][j] = flagnum[0]
    else:
        return
    
    for item in flag:
        curx, cury = i + item[0], j+item[1]
        if curx >= 0 and curx < m and cury >= 0 and cury < n:
            dfs(data, curx, cury, res, m, n, flag, flagnum)
flag = [[-1, 0], [1, 0], [0, -1], [0, 1]]
flagnum = [10]
resdict = {}
for i in range(m):
    for j in range(n):
        if data[i][j] == 1:
            res = [0]
            dfs(data, i, j, res, m, n, flag, flagnum)
            resdict[flagnum[0]] = res[0]
            flagnum[0] +=1
            ress.append(res[0])
            
print resdict
print ress
maxnum = 0
total = sum(ress)
for i in range(m):
    for j in range(n):
        if data[i][j] == 0:
            temp = set()
            for item in flag:
                curx, cury = i + item[0], j + item[1]
                if curx >= 0 and curx < m and cury >= 0 and cury < n and data[curx][cury] != 0:
                    temp.add(data[curx][cury])
            templ = []
            if temp:
                for key in list(temp):
                    templ.append(resdict[key])
                
                templ.sort()
                if len(templ) >= 2 :
                    datanum =  templ[-2] + templ[-1] + 1
                    if datanum <= total:
                        maxnum = max(datanum, maxnum)
                    
                    
print maxnum


