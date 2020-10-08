data = raw_input()

flag = {'(':')', '[':']', '{':'}'}

res = []
flag_res = True
for char in data:
    if char in flag.keys():
        res.append(char)
    else:
        if res:
            if flag[res[-1]] == char:
                res.pop()
                continue
            else:
                flag_res = False
                break
        else:
            flag_res = False
            break

print flag_res
