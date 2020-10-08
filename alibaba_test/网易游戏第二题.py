data = raw_input()

lists = []
i, j = 0, 0
while j < len(data):
    while  j < len(data) and data[j] == data[i]:
        j +=1
    temp = data[i:j]
    length = len(temp)
    if length < 4:
        lists.append(temp)
    elif length < 30:
        lists.append('0'+ chr(ord('a')+length-4) +temp[0])
    elif length <= 55:
        lists.append('0' + chr(ord('A') + length - 30) + temp[0])
    elif length > 55:
        res1 = '0Z' + temp[0]
        flag = length%55
        if flag < 4:
            res2 = temp[0]*flag
        elif flag < 30:
            res2 = '0'+ chr(ord('a')+flag-4) +temp[0]
        else:
            res2 = '0' + chr(ord('A') + flag - 30) + temp[0]
        lists.append(res1*(length/55) + res2)
    i = j
print lists
print ''.join(lists)


