class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        import math
        n, m = len(matrix), len(matrix[0])
        
        i = 0
        res = []
        while i < int(math.ceil(min(n, m)/2.0)):
            self.printfNums(res, i, m - 2 * i, n - 2 * i, matrix)
            i += 1
        return res
    
    def printfNums(self, res, i, x, y, matrix):
        
        for j in range(i, i+x):
            res.append(matrix[i][j])
        
        for k in range(i+1, y +i):
            res.append(matrix[k][i + x - 1])
            
        if y > 1:
            for h in list(range(i, x - 1 + i))[::-1]:
                res.append(matrix[i + y - 1][h])
        
        if x > 1:
            for g in list(range(i + 1, i + y - 1))[::-1]:
                res.append(matrix[g][i])
a = [[7],[9],[6]]
print Solution().spiralOrder(a)