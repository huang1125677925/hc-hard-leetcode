n = int(raw_input())
a = map(int, list(raw_input()))
b = map(int, list(raw_input()))
from collections import Counter
flag = set(b)
flagdict = Counter(b)
res = ''
for i in range(len(a)):
    temp = int(a[i])
    while temp <= 9:
        if temp in flag and flagdict[temp]:
            res += str(temp)
            flagdict[temp] = flagdict[temp]-1
            break
        else:
            temp+=1
    if temp == 10:
        while res:
            temp1 = int(res[-1])
            res = res[:-1]
            flagdict[temp1] +=1
            temp1 +=1
            while temp1 <= 9:
                if temp1 in flag and flagdict[temp1]:
                    res += str(temp1)
                    flagdict[temp1] -= 1
                    break
                else:
                    temp1 += 1
            if temp1 <= 9:
                temp = []
                for key, value in flagdict.items():
                    temp.extend([str(key)] * value)
                temp.sort()
                res += ''.join(temp)
                break
            else:
                continue
        if res == '':
            res = -1
        break
    elif temp == a[i]:
        continue
    elif temp > a[i]:
        temp = []
        for key, value in flagdict.items():
            temp.extend([str(key)]*value)
        temp.sort()
        res += ''.join(temp)
        break

print int(res)

n = int(raw_input())
a = map(int, list(raw_input()))
b = map(int, list(raw_input()))
from collections import Counter
flag = set(b)
flagdict = Counter(b)
res = ''
for i in range(len(a)):
    temp = int(a[i])
    while temp <= 9:
        if temp in flag and flagdict[temp]:
            res += str(temp)
            flagdict[temp] = flagdict[temp]-1
            break
        else:
            temp+=1
    if temp == 10:
        res = -1
        break
    elif temp == a[i]:
        continue
    elif temp > a[i]:
        temp = []
        for key, value in flagdict.items():
            temp.extend([str(key)]*value)
        temp.sort()
        res += ''.join(temp)
        break

print int(res)




