def cmp1(x, y):
    return x + y < y + x
class LargerNumKey(str):
    def __lt__(x, y):
        return x + y < y + x
nums = [3,30,34,5,9, 1]
nums = list(map(str, nums))
nums = sorted(nums, key=LargerNumKey)
print ''.join(nums)