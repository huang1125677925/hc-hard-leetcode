class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        n = len(A)
        if n == L + M:
            return sum(A)
        
        l, s = max(L, M), min(L, M)
        max_sum = 0
        for i in range(l, n + 1):
            res = sum(A[i - l:i])
            
            left, right = A[:i-l], A[i:]
            
            if len(left) >= s:
                for j in range(s, len(left)+1):
                    max_sum = max(max_sum, sum(left[j - s:j]) + res)
            if len(right) >= s:
                for j in range(s, len(right)+1):
                    max_sum = max(max_sum, sum(right[j - s:j]) + res)
        return max_sum
    

A, L, M = [2,1,5,6,0,9,5,0,3,8], 4, 3

print Solution().maxSumTwoNoOverlap(A, L, M)