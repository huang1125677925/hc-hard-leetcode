nums1 = map(int, raw_input().split())
nums2 = map(int, raw_input().split())

res = 10000000
n = len(nums2)
for j in range(n-2, -1, -1):
    if nums2[j] <= nums2[j+1]:
        continue
    else:
        nums2[j] = nums2[j+1]
for i in range(len(nums1)-1):
    res = min(res, nums1[i]+nums2[i+1])

print res