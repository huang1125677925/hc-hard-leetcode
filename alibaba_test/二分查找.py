import bisect


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = 0
        for i in range(len(nums) - 2):
            res += self.find(nums, i + 1, target - nums[i])
        
        return res
    
    def find(self, nums, i, target):
        res = 0
        for j in range(i, len(nums) - 1):
            temp = bisect.bisect_left(nums, target - nums[j]) -1
            if temp > j:
                res += temp - j
        return res
    

print Solution().threeSumSmaller([-2,0,1,3], 2)