data = map(int, raw_input().split())
data.sort()
data = data[::-1]
flag = {}
res = 0
for i in range(7):
    if i not in flag.keys():
        flag[i] = []
for i in range(len(data)):
    temp = data[i]%7
    if temp == 0:
        res += data[i]
    elif flag[7-temp]:
        num = flag[7 - temp].pop(0)
        res +=  num + data[i]
    else:
        flag[temp].append(data[i])
for i in range(1, 7):
    if flag[i]:
        j = len(flag[i]) - len(flag[i])%7
        res += sum(flag[i][:j])

if res == 0:
    print -1
else:
    print res