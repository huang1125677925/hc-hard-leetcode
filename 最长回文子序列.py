#encoding=utf-8
#代码写的没有意义也简直就是在坑自己，自己写的代码等过段时间就看不懂了
s='abba'
l=len(s)
d=[[0 for _ in range(l)] for _ in range(l)]
ans=0
def find_largest_sequence(s):
    for i in range(l):
        d[i][i]=1
        if i<l-1 and s[i]==s[i+1]:
            d[i][i+1]=1
            ans=2
    
    # 状态转移方程
    for L in range(3,l+1):
        # j代表的是每种长度比对时尾端的索引号
        #k代表首端的索引号，然后比对尾端和和首端是否相等，并且其中的部分是否相等
        for i in range(l-L+1):
            k=i+L-1
            if s[i]==s[k] and d[i+1][k-1]==1:
                d[i][k] = 1
                ans=L
    
    return  ans

# print find_largest_sequence(s)


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words_dict = {word: True for word in words}
        words = sorted(words, key=lambda i: len(i), reverse=True)
        
        for word in words:
            if self.canbuildword(word, True, words_dict):
                return word
        
        return ''
    
    def canbuildword(self, word, isOriginalWorld, words_dict):
        if word in words_dict.keys() and not isOriginalWorld:
            return words_dict[word]
        
        for i in range(1, len(word)):
            left, right = word[:i], word[i:]
            if left in words_dict.keys() and words_dict[left] and self.canbuildword(right, False, words_dict):
                return True
        
        words_dict[word] = False
        return False


class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        flag = [[0] * n for _ in range(n)]
        res = [0, '']
        for i in range(n):
            flag[i][i] = 1
            if res[0] < 1:
                res = [1, s[i]]
            if i < n - 1 and s[i] == s[i + 1]:
                flag[i][i + 1] = 1
                if res[0] < 2:
                    res = [2, s[i: i + 2]]
        
        for i in range(3, n+1):
            for j in range(n - i + 1):
                start, end = j, j + i - 1
                if s[start] == s[end] and flag[start + 1][end - 1] == 1:
                    flag[start][end] = 1
                    if res[0] < i:
                        res = [i, s[start:end + 1]]
        
        return res[1]
# print Solution().longestWord(["cat","banana","dog","nana","walk","walker","dogwalker"])

# a = ["qlmql","qlmqlmqqlqmqqlq","mqqlqmqqlqmqqlq","mqqlq","mqqlqlmlsmqq","qmlmmmmsm","lmlsmqq","slmsqq","mslqssl","mqqlqmqqlq"]
# a.sort(key = lambda x:len(x))
# a = a[::-1]
# print a

print Solution2().longestPalindrome("ccc")