path = raw_input()

flag = {'E':[1, 0], 'W':[-1, 0], 'N':[0, 1], 'S':[0, -1]}


flag_path = set()
start = [0, 0]
flag_path.add(tuple(start))
flag_res = False
for char in path:
    start[0] +=flag[char][0]
    start[1] +=flag[char][1]
    if tuple(start) in flag_path:
        flag_res = True
        break
    flag_path.add(tuple(start))

print flag_res

