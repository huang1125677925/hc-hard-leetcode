from collections import Counter


class Solution:
    def commonChars(self, chars):
        # write code here
        flag = Counter(chars[0])
        for i in range(1, len(chars)):
            temp1 = {}
            temp = Counter(chars[i])
            for key in set(flag.keys()) & set(temp.keys()):
                    temp1[key] = min(temp[key], flag[key])
            flag = temp1
        
        res = ''
        keys = flag.keys()
        keys.sort()
        for key in keys:
            res += key * flag[key]
        
        
        
        return res
    

print Solution().commonChars(["bella","label","roller"])