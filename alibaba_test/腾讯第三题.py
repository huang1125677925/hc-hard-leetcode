n = int(raw_input())
data = []
for i in range(n):
    num = int(raw_input())
    data.append(num)
    
def find(num):
    if num <= 10:
        return num
    temp = 10**(len(str(num))-1)
    res = (num/temp)*temp -1
    return sum(map(int, list(str(res)) + list(str(num-res))))

res = []
for num in data:
    res.append(find(num))
    
for r in res:
    print r
#
# n = int(raw_input())
# data = []
# for i in range(n):
#     num = int(raw_input())
#     data.append(num)
#
#
# def find(num):
#     mid = num / 2
#     res = 0
#     while mid < num:
#         res = max(res, sum(map(int, list(str(mid)) + list(str(num - mid)))))
#         mid += 1
#
#     return res
#
#
# res = []
# for num in data:
#     res.append(find(num))
#
# for r in res:
#     print r