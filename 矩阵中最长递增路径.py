#encoding=utf-8
#给定一个整数矩阵，找出最长递增路径的长度。

# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        res = [0]
        if matrix == []:
            return 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                self.dfs(res, matrix, i, j, [])
        
        return res[0]
    
    def dfs(self, res, matrix, i, j, path):
        m, n = len(matrix), len(matrix[0])
        if i >= m or i < 0 or j >= n or j < 0:
            if len(path) > res[0]:
                res[0] = len(path)
            return
        
        if path == []:
            path = path + [matrix[i][j]]
        elif matrix[i][j] > path[-1]:
            path = path + [matrix[i][j]]
        elif matrix[i][j] <= path[-1]:
            if len(path) > res[0]:
                res[0] = len(path)
            return
        
        self.dfs(res, matrix, i + 1, j, path)
        self.dfs(res, matrix, i - 1, j, path)
        self.dfs(res, matrix, i, j + 1, path)
        self.dfs(res, matrix, i, j - 1, path)

# 代码超时
matrix = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]

print Solution().longestIncreasingPath(matrix)


class Solution:
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        @lru_cache(None)
        def dfs(row: int, column: int) -> int:
            best = 1
            for dx, dy in Solution.DIRS:
                newRow, newColumn = row + dx, column + dy
                if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[row][column]:
                    best = max(best, dfs(newRow, newColumn) + 1)
            return best
        
        ans = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                ans = max(ans, dfs(i, j))
        return ans

