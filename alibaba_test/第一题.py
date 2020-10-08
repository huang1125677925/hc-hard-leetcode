n = int(raw_input())
import math
data = [1, 1]

while len(data) < n**2:
    data.append(data[-1]+data[-2])
    
data = data[::-1]

res = [[0]*n for _ in range(n)]

flag, i = n, 0

while i < math.ceil(n/float(2)):
    
    for up in range(i, n-i):
        res[i][up] = data.pop(0)
    
    for right in range(i+1, n-i):
        res[right][n-i-1] = data.pop(0)
        
    for down in range(n-i-2, i-1, -1):
        res[n-i-1][down] = data.pop(0)
    
    for left in range(n-i-2, i, -1):
        res[left][i] = data.pop(0)
    
    i +=1
        

print res


    


