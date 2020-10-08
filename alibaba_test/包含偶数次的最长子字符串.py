class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        resdict = {}
        flagnum = [0, 0, 0, 0, 0]
        for i in range(len(s)):
            if s[i] in flag.keys():
                flagnum[flag[s[i]]] = (flagnum[flag[s[i]]] + 1) % 2
            temp = int(''.join(map(str, flagnum)), 2)
            if temp not in resdict.keys():
                resdict[temp] = []
            resdict[temp].append(i)
        
        res = 0
        for key in resdict.keys():
            if len(resdict[key]) > 1:
                res = max(res, resdict[key][-1] - resdict[key][0])
        
        return res
    
print Solution().findTheLongestSubstring("leetcodeisgreat")