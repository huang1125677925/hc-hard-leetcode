n = int(raw_input())
data = map(int, raw_input().split())
time = int(raw_input())

data.sort()
if n % 2 == 1:
    res = data[0]
    data = data[1:]
    res += sum([data[i + 1] for i in range(0, n - 1, 2)])
else:
    res = sum([data[i + 1] for i in range(0, n, 2)])

if res <= time:
    print 1
else:
    print 0