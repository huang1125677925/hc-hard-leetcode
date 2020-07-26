#encoding=utf-8
# 给定一个由n个不重复非空字符串组成的数组，你需要按照以下规则为每个单词生成最小的缩写。
#
# 初始缩写由起始字母+省略字母的数量+结尾字母组成。
# 若存在冲突，亦即多于一个单词有同样的缩写，则使用更长的前缀代替首字母，直到从单词到缩写的映射唯一。换而言之，最终的缩写必须只能映射到一个单词。
# 若缩写并不比原单词更短，则保留原样。


# 输入: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
# 输出: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/word-abbreviation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 解法1，贪心法

words = ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
class Solution(object):
    def wordsAbbreviation(self, words):
        def abbrev(word, i = 0):
            if (len(word) - i <= 3): return word
            return word[:i+1] + str(len(word) - i - 2) + word[-1]

        N = len(words)
        ans = map(abbrev, words)
        prefix = [0] * N

        for i in xrange(N):
            while True:
                dupes = set()
                for j in xrange(i+1, N):
                    if ans[i] == ans[j]:
                        dupes.add(j)

                if not dupes: break
                dupes.add(i)
                for k in dupes:
                    prefix[k] += 1
                    ans[k] = abbrev(words[k], prefix[k])

        return ans
    

print Solution().wordsAbbreviation(words)


