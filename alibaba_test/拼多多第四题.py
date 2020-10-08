n, m = map(int, raw_input().split())
data = []
for i in range(m):
    temp = int(raw_input())
    data.append(temp)
    
data.sort()
index = [1] * m
res = set([0])
max_num = 0
while max_num <= n:
    temp = [index[i]*data[i] for i in range(m)]
    temp1 = min(temp)
    res.add(temp1)
    tempindex = temp.index(temp1)
    index[tempindex] +=1
    max_num = temp1
    

print len(res)-2
# n, m = map(int, raw_input().split())
# data = []
# for i in range(m):
#     temp = int(raw_input())
#     data.append(temp)
#
# data.sort()
# res = set()
# for i in range(1, n + 1):
#     for item in data:
#         if i >= item:
#             if i % item == 0:
#                 res.add(i)
#         else:
#             break
#
# print len(res)
#