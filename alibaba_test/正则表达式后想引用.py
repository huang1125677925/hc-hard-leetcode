n = int(raw_input())

input_data = []
for i in range(n):
    string = raw_input()
    input_data.append(list(string))

flag = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def dfs(nums, i, j, res, path, index, flag):
    if index == 5:
        res[0] += 1
        return
    
    for k in range(4):
        x, y = i+flag[k][0], j+flag[k][1]
        temp = path[index]
        if 0<=x and x<n and y>=0 and y<n and nums[x][y] == temp:
            dfs(nums, x, y, res, path, index+1, flag)
res, path = [0], ['C', 'H', 'I', 'N', 'A']
for i in range(n):
    for j in range(n):
        if input_data[i][j] == path[0]:
            dfs(input_data, i, j, res, path, 1, flag)
        


print res