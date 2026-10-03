class Solution(object):
    def sortColors(self, nums):
        l = 0
        r = 0
        n = len(nums)-1
        while r <=n :
            if nums[r]==0:
                nums[l],nums[r] = nums[r], nums[l]
                l+=1
                r+=1
            elif nums[r]==1:
                r+=1
            else: 
                nums[r],nums[n] = nums[n], nums[r]
                n-=1
        return nums