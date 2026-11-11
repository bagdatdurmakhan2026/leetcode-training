class Solution(object):
    def res(self, nums):
        l,r =0,0
        lm = len(nums)-1
        while True:
            l = nums[l]
            r = nums[nums[r]]
            if l == r:
                break
        l = 0
        while l!=r:
            l = nums[l]
            r = nums[r]
        return l       
nums = [1,3,4,2,2]
ans = Solution().res(nums)
print(ans)
