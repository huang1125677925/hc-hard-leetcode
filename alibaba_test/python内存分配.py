import math

m, n = map(int, raw_input().split())

for i in range(1, 501):
    a = math.sqrt(i+m)
    b = math.sqrt(i+n)
    if int(a) == a and int(b) == b:
        print i
        break
    