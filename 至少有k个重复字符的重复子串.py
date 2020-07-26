#encoding=urf-8
# 找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。
#
# 示例 1:
#
# 输入:
# s = "aaabb", k = 3
#
# 输出:
# 3
#
# 最长子串为 "aaa" ，其中 'a' 重复了 3 次。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def longestSubstring(self, s, k):
        if not s:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)
    
# 用分治法解决