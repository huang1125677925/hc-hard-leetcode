

def dfs(flag, size, startx, starty, n, res, cur):
    if n == 0:
        res.append(cur)
        return

    for item in flag:
        tempx = startx + item[0]
        tempy = starty + item[1]
        if tempx >= 0 and tempx < size and tempy >= 0 and tempy < size:
            dfs(flag, size, tempx, tempy, n - 1, res, cur * (0.25))
    
string = 'abch kkk'
string.endswith()
def how_likely_alive(size, startx, starty, n):
    if n == 0:
        return 1
    
    flag = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    res = []
    cur = 1
    dfs(flag, size, startx, starty, n, res, cur)
    
    
    return sum(res)
    

print how_likely_alive(3, 0, 0, 2)