class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        l = list(range(1, maxChoosableInteger + 1))
        target = desiredTotal
        
        def dfs(l, target, path,res):
            if path and sum(path) >= target:
                if len(path) % 2 == 1:
                    res.append(True)
                
            if l:
                a = l[0]
                dfs(l[1:], target, path+[a],res)
                dfs(l[1:], target, path,res)
            
        res=[]
        dfs(l, target, [],res)
        return res
    

print(Solution().canIWin(10,11))