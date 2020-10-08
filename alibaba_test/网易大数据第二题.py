l1 = raw_input().split()
l2 = raw_input().split()
l3 = raw_input().split()

res = set(l3) - set(l2) - set(l1)

print len(res)