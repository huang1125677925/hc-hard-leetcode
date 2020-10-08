#encoding=utf-8
# 2^32


def add(a, b):
    MASK = 0x100000000
    # 整型最大值
    MAX_INT = 0x7FFFFFFF
    MIN_INT = MAX_INT + 1
    while b != 0:
        # 计算进位
        carry = (a & b) << 1
        # 取余范围限制在 [0, 2^32-1] 范围内
        a = (a ^ b) % MASK
        b = carry % MASK
    return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)

def div(a, b):
    flag = True if (a^b)>=0 else False  # 同号时flag为True
    if a<0:
        a = add(~a, 1)
    if b<0:
        b = add(~b, 1)
    res = 0
    for i in range(31, -1, -1):
        if a>=(b<<i):
            res = add(res, 1<<i)
            a = a - b<<i
    return res if flag else add(~res,1)


print div(3, 1)