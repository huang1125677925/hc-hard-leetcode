#encoding=utf-8
fo = open("../360.py", "rw")
print "文件名为: ", fo.name

print fo.readline()
# line = fo.read()
# print "读取的字符串: %s" % (line)
fo.seek(110)
print fo.readline()

# print fo.readline()
# print '-----------------------------'*10
# print fo.readlines()
# print '_'*1000

# 关闭文件
fo.close()

