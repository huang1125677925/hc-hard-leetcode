class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        flag, stack = [0], []
        
        for item in hours:
            if item > 8:
                flag.append(1 + flag[-1])
            else:
                flag.append(-1 + flag[-1])
        stack = [0]
        for i in range(1, len(flag)):
            if flag[i] < flag[stack[-1]]:
                stack.append(i)
        ans = 0
        j = len(flag) - 1
        while j > 0:
            while stack and flag[j] - flag[stack[-1]] > 0:
                ans = max(ans, j - stack[-1])
                stack.pop()
            if stack and j <= stack[-1]:
                stack.pop()
            j -= 1
        
        return ans
    
print Solution().longestWPI(
[6,6,9])