n = map(int, raw_input())[0]
data = []
for i in range(n):
    temp = map(int, raw_input())[0]
    data.append(temp)
data.sort()
while data[-1] != 0:
    index = 0
    for i in range(n):
        if data[i] != 0:
            index = i
            break
    min_num = min(data[index:])
    print min_num
    for i in range(index, n):
        if data[i] >= min_num:
            data[i] = data[i] - min_num
