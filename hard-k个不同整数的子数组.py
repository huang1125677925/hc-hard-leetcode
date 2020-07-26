#encoding=utf-8
# 给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定独立的子数组为好子数组。
#
# （例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。）
#
# 返回 A 中好子数组的数目。

# 输入：A = [1,2,1,2,3], K = 2
# 输出：7
# 解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].


# 输入：A = [1,2,1,3,4], K = 3
# 输出：3
# 解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].


# 至少需要k个数字组成的子数组，才能得到答案
# 但是k个数字不一定够，所以可能会更长
# 可以先枚举出所有的可能的子数组，然后再验证一下，如果前面的超了，那么后边的肯定没有必要再遍历了，
# 超时，有没有更好的办法了？
class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n, res = len(A), 0
        
        for i in range(n - K + 1):
            temp = set()
            temp.add(A[i])
            j = i + 1
            if j == n and len(temp) == K:
                res += 1
            while j < n:
                if len(temp) == K:
                    res += 1
                if len(temp) > K:
                    break
                temp.add(A[j])
                j += 1
                if j == n and len(temp) == K:
                    res += 1
        
        return res

class Solution1:
    def subarraysWithKDistinct(self, A, K):
        #  都没看懂这个写的是什么
        from collections import Counter
        def atMost(A, K):
            count = Counter()
            res = i = 0
            for j, num in enumerate(A):
                if count[num] == 0:
                    K -= 1
                count[num] += 1
                while K < 0:
                    count[A[i]] -= 1
                    if count[A[i]] == 0:
                        K += 1
                    i += 1
                res += j - i + 1
            return res
        return atMost(A, K) - atMost(A, K-1)


A = [1,2, 3, 4]
K = 1
print Solution1().subarraysWithKDistinct(A, K)
