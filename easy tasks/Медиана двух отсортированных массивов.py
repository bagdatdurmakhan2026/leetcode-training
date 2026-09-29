import numpy as np
class Solution(object):
    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
    def r(self):
        arr = []
        arr = self.nums1+self.nums2
        return arr
nums1 =[int(x) for x in input().split(",")]
nums2 =[int(y) for y in input().split(",")]
res = Solution(nums1,nums2)
ser = res.r()
nas = (np.median(ser))
print(nas)