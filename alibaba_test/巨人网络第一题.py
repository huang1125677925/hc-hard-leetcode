def sort1(nums):
    l, r, k = 0, len(nums) - 1, 0
    
    while l < r:
        if nums[l] == 2 and nums[r] == 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            k += 1
        elif nums[l] == 0:
            l += 1
            k += 1
        elif nums[r] == 2:
            r -= 1
        elif nums[r] ==0 or nums[l] == 2:
            if nums[l] == 2:
            
        elif (nums[l] == 1 or nums[r] == 1) and nums[k] == 1:
            k += 1
        elif (nums[l] == 1 or nums[r] == 1) and nums[k] != 1:
            if nums[k] == 2 and k < r:
                nums[k], nums[r] = nums[r], nums[l]
                r -= 1
            elif nums[k] == 0 and k > l:
                nums[l], nums[k] = nums[k], nums[l]
                l += 1


if __name__ == "__main__":
    nums = [2, 2, 0, 0, 1, 1, 0]
    sort1(nums)
    print nums

# 5
# 0.01
# 5.00
# 55.00
# 4.00
# 999.99
# [0.01, 0.01, 5.0, 4.0, 55.0]