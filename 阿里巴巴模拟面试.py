#encoding=utf-8
class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        
        l = len(A)
        if l == 1:
            return 0
        res = 0
        if A[0] > A[1] or B[0] > B[1]:
            A[0], B[0] = B[0], A[0]
            res += 1
        
        for i in range(1, l - 1):
            if A[i] <= A[i - 1] or A[i] >= A[i + 1] or B[i] <= B[i - 1] or B[i] >= B[i + 1]:
                A[i], B[i] = B[i], A[i]
                res += 1
        
        if A[-1] <= A[-2] or B[-1] <= B[-2]:
            res += 1
        return res
    
class Solution1(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        arr = []
        res = 0
        for num in nums:
            res += len(arr) - bisect.bisect_left(arr, num * 2)
            # bisect.insort(arr, num)
            loc = bisect.bisect_left(arr, num)
            arr[loc:loc] = [num]
        return res


class Solution2(object):
    def permutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        s = list(S)
        self.dfs(s, res, '')
        return res

    def dfs(self, s, res, path):
        if s == []:
            res.append(path)
            return

        for i in range(len(s)):
            self.dfs(s[:i] + s[i + 1:], res, path + s[i])
        
        

A = [0,4,4,5,9]
B = [0,1,6,8,10]


class Solution3(object):
    def getKthMagicNumber(self, k):
        """
        :type k: int
        :rtype: int
        """
        res = [1]
        flag = set([1])
        if k == 1:
            return res[0]
        index3, index5, index7 = 0, 0, 0
        
        while len(res) < k:
            temp = min(res[index3] * 3, res[index5] * 5, res[index7] * 7)
            if res[index3] * 3 == temp:
                index3+=1
            elif res[index5] * 5 == temp:
                index5 += 1
            elif res[index7] * 7 == temp:
                index7 += 1
            if temp not in flag:
                res.append(temp)
                flag.add(temp)
        print res
        return res[-1]
    
class eightscreen(object):
    def main(self, n):
        res = []
        self.dfs(list(range(0, n)), res, [])
        return res
    
    def dfs(self, nums, res, path):
        if len(path) > 1:
            for i in range(len(path)-1):
                if abs(path[-1] - path[i]) == len(path) - i -1:
                    return
                
        if nums == []:
            res.append(path)
            return
        
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], res,  path + [nums[i]])


class Solution4:
    def generateParenthesis(self, n):
        re = []
        state = ''
        
        def dsp(state, p, q):  # p,q分别表示(和)还剩的个数，有个隐含条件：就是(在组合时候比)用的多或相等
            if p > q:  # 非法，剪枝
                return
            if q == 0:  # )用完之时
                re.append(state)
            
            if p > 0:
                dsp(state + '(', p - 1, q)
            if q > 0:
                dsp(state + ')', p, q - 1)
        
        dsp(state, n, n)
        return re


class Solution5(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = len(nums)
        if l == 1:
            return nums[0] + k
        
        temp = []
        for i in range(1, l):
            temp_num = nums[i] - nums[i - 1]
            for i in range(temp_num):
                temp.append(nums[i - 1] + i + 1)
                if len(temp) == k:
                    return temp[-1]
        
        if len(temp) < k:
            return nums[-1] + k - len(temp)

print Solution5().missingElement([4,7,9,10], 1)
