n = int(raw_input())
res = 0
while n > 0:
    temp = n
    if temp%5  == 0:
        while temp%5 == 0 and temp > 0:
            res +=1
            temp = temp/5
    n -=1
print res