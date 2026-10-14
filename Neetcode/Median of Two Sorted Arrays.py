class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        ans = sorted(nums1+nums2)
        n = len(ans)
        mid  = n//2
        if n % 2 == 0:
            return (ans[mid - 1] + ans[mid]) / 2.0
        else:
            return float(ans[mid])
        