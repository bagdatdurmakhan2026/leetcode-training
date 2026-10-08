class Solution(object):
    def ans(self, nums):
        n = len(nums)
        mn = float('inf')
        ans = 0
        for i in nums:
            if nums[i] < mn:
                mn = nums[i]
            elif i - mn > ans:
                ans = i - mn
        return ans
                