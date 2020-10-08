n = int(raw_input())

data = [[100]*n for _ in range(n)]
temp = n/2

if n%2 ==0:
    for i in range(n):
        data[i][i] = 0
        data[i][n-i-1] = 0
    
    for i in range(temp):
        index1 = data[i].index(0)
        index2 = data[i].index(0, index1+1)
        if index1 == 0 and index2 == n-1:
            for j in range(index1+1, temp):
                data[i][j] = 2
            for j in range(temp, index2):
                data[i][j] = 1
        elif index1 > 0 and index2 < n-1:
            for j in range(0, index1):
                data[i][j] = 3
            for j in range(index1+1, temp):
                data[i][j] = 2
            for j in range(temp, index2):
                data[i][j] = 1
            for j in range(index2+1, n):
                data[i][j] = 8
    
    for i in range(temp, n):
        index1 = data[i].index(0)
        index2 = data[i].index(0, index1+1)
        if index1 == 0 and index2 == n - 1:
            for j in range(index1 + 1, temp):
                data[i][j] = 5
            for j in range(temp, index2):
                data[i][j] = 6
        elif index1 > 0 and index2 < n - 1:
            for j in range(0, index1):
                data[i][j] = 4
            for j in range(index1 + 1, temp):
                data[i][j] = 5
            for j in range(temp, index2):
                data[i][j] = 6
            for j in range(index2+1, n):
                data[i][j] = 7
elif n % 2 == 1:
    for i in range(n):
        data[i][i] = 0
        data[i][n - i - 1] = 0
        data[i][temp] = 0
        data[temp][i] = 0
    
    for i in range(temp):
        index1 = data[i].index(0)
        index2 = data[i].index(0, temp+1)
        
        if index1 == 0 and index2 == n - 1:
            for j in range(index1 + 1, temp):
                data[i][j] = 2
            for j in range(temp+1, index2):
                data[i][j] = 1
        if index1 > 0 and index2 < n - 1:
            for j in range(0, index1):
                data[i][j] = 3
            for j in range(index1 + 1, temp):
                data[i][j] = 2
            for j in range(temp+1, index2):
                data[i][j] = 1
            for j in range(index2+1, n):
                data[i][j] = 8
    
    for i in range(temp+1, n):
        index1 = data[i].index(0)
        index2 = data[i].index(0, temp+1)
        if index1 == 0 and index2 == n - 1:
            for j in range(index1 + 1, temp):
                data[i][j] = 5
            for j in range(temp+1, index2):
                data[i][j] = 6
        if index1 > 0 and index2 < n - 1:
            for j in range(0, index1):
                data[i][j] = 4
            for j in range(index1 + 1, temp):
                data[i][j] = 5
            for j in range(temp+1, index2):
                data[i][j] = 6
            for j in range(index2+1, n):
                data[i][j] = 7
    

for item in data:
    print ' '.join(map(str, item))
