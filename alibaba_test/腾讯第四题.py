n = int(raw_input())
data = map(int, raw_input().split())

res = min(data)
for i in range(len(data)):
    data[i] -= res
    
while sum(data) != 0:
    start, end = 0, 0
    while end <= n:
        if end !=n and data[end] > 0:
            end +=1
        elif end!=n and data[end] == 0 and start == end:
            end +=1
            start +=1
        elif end !=n and data[end] == 0 and end > start:
            temp = min(data[start:end])
            res += temp
            for i in range(start, end):
                data[i] -= temp
            end = end +1
            start = end
        elif end == n and end > start:
            temp = min(data[start:end])
            res += temp
            for i in range(start, end):
                data[i] -= temp
            end = end + 1
            start = end
            
print res
