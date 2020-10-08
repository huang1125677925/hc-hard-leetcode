n = raw_input()

flag = ''
if n[0] == '-':
    flag += n[0]
    n = n[1:]
    
res = 0
listn = list(n)
listn = listn[::-1]
for i in range(len(listn)):
    if listn[i].isdigit():
        res += (ord(listn[i])-ord('0'))*(36**i)
    elif listn[i].isalpha():
        res += (ord(listn[i])-ord('a') + 10)*(36**i)
    else:
        res = 0
        break

maxnum = 9223372036854775807
minnum = -9223372036854775807

if flag == '-':
    res = res*(-1)
    
if res > maxnum:
    print maxnum
elif res < minnum:
    print minnum
else:
    print res

