#encoding=utf-8
def customer():
    while True:
        number = yield
        print '开始消费：', number


custom = customer()
next(custom)
for i in range(10):
    print '开始生产：', i
    custom.send(i)