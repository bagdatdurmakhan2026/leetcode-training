class Solution(object):
    def maxSubArray(self, nums):
        mx = float('-inf')
        n = len(nums)
        for i in range(n):
            ans = 0
            for j in range(i,n):
                ans+=nums[j]
                mx = max(mx,ans)
        return mx      
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))