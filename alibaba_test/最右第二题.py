n = int(raw_input())

temp = [1, 2, 5]
if n <=len(temp):
    print temp[n-1]
else:
    while len(temp) < n:
        tempn = len(temp) + 1
        templ = []
        tempd = range(tempn)
        for i in range(tempn):
            left, right = len(tempd[:i]), len(tempd[i+1:])
            if left > 0:
                left = left -1
            if right > 0:
                right = right-1
            templ.append(temp[left]*temp[right])
        temp.append(sum(templ))
    print temp[n-1]