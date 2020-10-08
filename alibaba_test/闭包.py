b = 100
def add(x):
    z = 100
    def add1(y):
        z1 = 100
        def add2(k):
            return b+x+y+k+z+z1
        return add2
    return add1

a = add(10)
a1 = a(10)
print a1(1)