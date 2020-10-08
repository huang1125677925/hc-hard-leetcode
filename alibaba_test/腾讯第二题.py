data = raw_input()
k = int(raw_input())
res = []
n = len(data)
for i in range(1, n+1):
    for j in range(n-i+1):
        temp = data[j:j+i]
        res.sort()
        if temp not in res and len(res) < k:
            res.append(temp)
        elif temp not in res and temp < res[-1]:
            res.pop()
            res.append(temp)
            


print res[k-1]
# data = raw_input()
# k = int(raw_input())
#
# res = set()
# n = len(data)
# for i in range(1, n + 1):
#     for j in range(n - i + 1):
#         if data[j:j + i] not in res:
#             res.add(data[j:j + i])
#
# res = list(res)
# res.sort()
# print res[k - 1]