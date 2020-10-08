#encoding=utf-8
class Solution(object):
    def canPartition(self, nums):
        if nums == []:
            return False
        length, sums = len(nums), sum(nums)
        if sums%2 == 1:
            return False
        else:
            target = sums/2

        dp = [[0]*(target+1) for _ in range(length)]

        # 先填表格第 0 行，第 1 个数只能让容积为它自己的背包恰好装满
        if (nums[0] <= target):
            dp[0][nums[0]] = 1

        # 再填表格后面几行
        for i in range(1, length):
            for j in range(0, target+1):
                 # 直接从上一行先把结果抄下来，然后再修正
                dp[i][j] = dp[i - 1][j]

                if (nums[i] == j):
                    dp[i][j] = 1
                    continue
                if (nums[i] < j):
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
        return dp[length - 1][target]


print Solution().canPartition([1, 2, 3, 5])