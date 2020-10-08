class Solution:
    def getPasswordCount(self , password ):
        nums = map(int, list(password))
        for i in range(10):
            res = [0]
            self.dfs(nums, res, [i])
            print i, res, len(password)
        
    def dfs(self, nums, res, path):
        if len(path) == len(nums) and nums <> path:
            res[0] +=1
            return
        elif len(path) == len(nums) and nums == path:
            return
        
        temp = nums[len(path)] + path[-1]
        if temp%2 == 0:
            self.dfs(nums, res, path + [temp/2])
        else:
            self.dfs(nums, res, path + [temp/2])
            self.dfs(nums, res, path + [temp/2 + 1])

print Solution().getPasswordCount('12345')


