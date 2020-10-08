


def find(num):
    res = []
    dfs(num, res, [])
    return len(res)
    
    
def dfs(num, res, path):
    if num == '':
        res.append(path)
        return
    
    if len(num) > 0:
        dfs(num[1:], res, path + [num[0]])
    
    if len(num) > 1 and num[0] != '0' and int(num[:2]) < 26:
        dfs(num[2:], res, path + [num[:2]])
        

print find('12158')