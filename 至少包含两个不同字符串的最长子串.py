#encoding=utf-8
# 其主要思想就是保持窗口中第一个字符的最新索引号，和第三个字符的最新索引号
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        n = len(s)
        if n < 3:
            return n
        left, right = 0, 0
        hashmap = defaultdict()
        max_len = 2
        while right < n:
            # slidewindow contains less than 3 characters
            if len(hashmap) < 3:
                hashmap[s[right]] = right
                right += 1

            # slidewindow contains 3 characters
            if len(hashmap) == 3:
                # delete the leftmost character
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len
    
s = "ccaacbbb"
print Solution().lengthOfLongestSubstringTwoDistinct(s)