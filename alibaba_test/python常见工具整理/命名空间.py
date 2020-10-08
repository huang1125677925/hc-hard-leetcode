#encoding=utf-8
Money = 2000


def AddMoney():
    # 想改正代码就取消以下注释:
    global Money
    print globals()
    print locals()
    Money = Money + 1


print Money
AddMoney()
print Money

print __name__
# print __dict__
