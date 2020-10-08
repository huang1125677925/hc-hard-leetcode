class Solution:
    
    def dfs(self, m, listnum, path, res):
        if len(path) == m-1:
            res.append(path)
            return
        if listnum == []:
            return
        
        self.dfs(m, listnum[1:], path + [listnum[0]], res)
        self.dfs(m, listnum[1:], path, res)
        
    def min_send(self , nums , m ):
        # write code here
        if m == 1:
            return sum(nums)
        
        listnum = range(1, len(nums))
        res = []
        self.dfs(m, listnum, [], res)
        reslist =[]
        for item in res:
            item = [0] + item + [len(nums)]
            temp = [sum(nums[item[i-1]:item[i]]) for i in range(1, m+1)]
            reslist.append(max(temp))
            
        return min(reslist)
        
    

print Solution().min_send([4,3,5,10,12],2)
