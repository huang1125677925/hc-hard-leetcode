n, m = map(int, raw_input().split())
operator = map(int, raw_input().split())

data = range(1, n+1)
flag = []
for i in range(m):
    if flag == []:
        flag.append([operator[i], 1])
    else:
        if operator[i] == flag[-1][0]:
            flag[-1][1] +=1
        else:
            flag.append([operator[i], 1])
            
def oper1(nums, n, cnt):
    temp = nums[:cnt]
    nums[:n-cnt] = nums[cnt:]
    nums[n-cnt:] = temp
    
def oper2(nums, n, cnt):
    if cnt % 2 == 1:
        for i in range(0, n, 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]

for num in flag:
    if num[0] == 1:
        oper1(data, n, num[1])
    else:
        oper2(data, n, num[1])
        
print ' '.join(map(str, data))
