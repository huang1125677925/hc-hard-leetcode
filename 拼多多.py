# m = map(int, raw_input())[0]
# data = map(int, raw_input().split())
#
# data.sort()
#
# i, j = 0, m-1
# temp = []
# while i < j:
#     temp.append(data[i]+data[j])
#     i += 1
#     j -= 1
#
# print abs(temp[0]-temp[-1])

# target = int(raw_input())
# normal = int(raw_input())
# buff = int(raw_input())
#
#
# def dfs(target, path, res):
#     if target <= 0:
#         if res:
#             res = min(sum(path), res[0])
#         else:
#             res.append(sum(path))
#         return
#
#     dfs(target - normal, path + [1], res)
#     dfs(target - buff, path + [2], res)
#
#
# res = []
# dfs(target, [], res)
#
# print res[0]

n = int(raw_input())
data = map(int, raw_input().split())
total = sum(data)
temp = [1]
data[0] = data[0] - 1
flag = True
while len(temp) < total:
    for i in range(n):
        if data[i] > 0 and i+1 != temp[-1]:
            temp.append(i + 1)
            data[i] = data[i] - 1
            print len(temp)
            print sum(data)
            print data
            break
    
    if len(temp) != total and data[i] >= 1 and i == temp[-1] and sum(data) == data[i]:
        flag = False
        break

if flag:
    print temp
else:
    print '-'

# from collections import Counter
#
# num_dict = Counter(list('999988833333331344'))
#
# print num_dict


