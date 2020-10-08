from abc import abstractmethod, ABCMeta

# class A(object):
#
#     def __new__(cls, *args):
#         a = []
#         for arg in args:
#             a.append(arg*10)
#             print("another arg through *argv:", arg)
#         print "A.__new__ called"
#         return super(A, cls).__new__( a)
#
#     def __init__(self):
#         print self.__sizeof__()

class Test1(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def overwrite(self):
        pass
    
    def printnum(self):
        for i in range(100):
            print i
            
class Test(Test1):
    
    def __new__(cls):
        return super(Test, cls).__new__(cls)
    
    def __init__(self):
        print id(self)
    
    def overwrite(self):
        print 'write'
    
    def printnum1(self):
        print type(self)

test = Test()
test.overwrite()
print id(test)
        
class int1(int):
    def __int__(self):
        pass
        


class Sample():
    
    def __init__(self):
        self.val = 10
        self.key = 'fuck'
    
    def __int__(self):
        return self.val*100
    
    def __float__(self):
        return self.val*1.0
    # def __str__(self):
    #     return "SAMPLE"
    
    
test1 = Sample()
print int(test1)
print float(test1)
print





