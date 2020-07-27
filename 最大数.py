class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=lambda x, y: x + y > y + x))
        return '0' if largest_num[0] == '0' else largest_num


print(Solution().largestNumber([3,30,34,5,9]))