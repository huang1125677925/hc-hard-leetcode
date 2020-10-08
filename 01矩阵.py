class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if matrix == []:
            return matrix
        
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                res = []
                if matrix[i][j] > 0:
                    self.dfs(matrix, i, j, m, n, res, [])
                    res = sorted(res, key=len)
                    matrix[i][j] = len(res[0])-1
        
        return matrix
    
    def dfs(self, matrix, i, j, m, n, res, path):
        if i < 0 or j < 0 or i >= m or j >= n:
            return
        if matrix[i][j] == 0:
            path = path + [0]
            res.append(path)
            return
        else:
            path.append(matrix[i][j])
        
        self.dfs(matrix, i + 1, j, m, n, res, path)
        self.dfs(matrix, i - 1, j, m, n, res, path)
        self.dfs(matrix, i, j + 1, m, n, res, path)
        self.dfs(matrix, i, j - 1, m, n, res, path)



matrix = [[0,0,0],[0,1,0],[1,1,1]]

print Solution().updateMatrix(matrix)