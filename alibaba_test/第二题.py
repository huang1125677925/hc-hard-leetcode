from collections import Counter
n, m = map(int, raw_input().split())
res = 0

# for i in range(n, m+1):
#     temp = str(i)
#     if temp[:-1] == temp[:-1][::-1]:
#         res +=1
#         continue
#     length = len(temp)
#     if length == 1:
#         continue
#     elif length == 2:
#         res +=1
#         continue
#     elif length == 3 or length == 4:
#         temp1 = Counter(temp).values()
#         if max(temp1) > 1:
#             res +=1
#             continue
#     elif length == 5 or length==6:
#         temp1 = Counter(temp).values()
#         if max(temp1) > 3 or min(temp1) >=2 or temp1.count(2) == 2:
#             res +=1
#             continue
#     else:
#         temp1 = Counter(temp).values()
#         temp2 = 0
#         for i in temp1:
#             if i%2 ==1:
#                 temp2+=1
#         if i == 1 or i ==2:
#             res+=1
#         continue

for i in range(n, m+1):
    temp = str(i)
    length = len(temp)
    if length == 1:
        continue
    elif length == 2:
        res +=1
        continue
    else:
        for i in range(length):
            temp1 = temp[:i] + temp[i+1:]
            if temp1 == temp1[::-1]:
                res +=1
                break
        continue

print res
        
        
