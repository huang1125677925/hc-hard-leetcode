class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        m, n = len(board), len(board[0])
        flag = [[0] * n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if self.dfs(i, j, board, word, flag, m, n):
                    return True
        
        return False
    
    def dfs(self, i, j, board, word, flag, m, n):
        if word == '':
            return True
        if i >= m or i < 0 or j >= n or j < 0 or flag[i][j]: return False
        if board[i][j] == word[0]:
            flag[i][j] = 1
            res = self.dfs(i + 1, j, board, word[1:], flag, m, n) or self.dfs(i - 1, j, board, word[1:], flag, m, n) \
                  or self.dfs(i, j + 1, board, word[1:], flag, m, n) or self.dfs(i, j - 1, board, word[1:], flag, m, n)
            flag[i][j] = 0
            return res
            
                   
board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"
print Solution().exist(board, word)