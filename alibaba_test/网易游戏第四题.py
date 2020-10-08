s, e = map(int, raw_input().split())

minl = [1000]
for i in range(1, s*2):
    temp = e%i + abs(s-i)
    templ = []
    if temp < minl[0]:
        templ.append(temp)
        flag = [s, i]
        if e%i != 0:
            flag.append(e-e%i)
        flag.append(e)
        templ.extend(flag)
        minl = templ

print minl[0]
print len(minl)-1
print minl[1:]
