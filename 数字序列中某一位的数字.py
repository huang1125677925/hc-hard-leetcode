class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        def printf(x, y, n):
            num = x + n/y
            index = n%y
            return int(str(num)[index])
        if n < 10: return n
        a = 2
        nums = 10
        while n >= nums:
            nums = nums + a*9*(10**(a-1))
            a +=1
        a = a-1
        n = n - (nums - a*9*(10**(a-1)))
        return printf(10**(a-1), a, n)
    

print Solution().findNthDigit(10000)