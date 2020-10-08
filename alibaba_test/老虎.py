


def judge(a, b, a1, b1):
    if b >= a1:
        return -1
    res = 0
    temp = a1
    while a > 0:
        if b >= a1:
            a1 = temp
            a1 -= b
            res +=1
        else:
            a1 -= b
            a -= b1
            res +=1
    
    return res

print judge(1,1,1,1)
