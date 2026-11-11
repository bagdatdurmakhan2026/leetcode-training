class Solution(object):
    def sortArrayByParity(self, nums):
        l = 0
        r = len(nums)-1
        while l < r :
            if nums[l]%2!=0:
                nums[l],nums[r] = nums[r],nums[l]
                r-=1
            else:
                l+=1
        return nums

nums = [0, 1, 2]
print(Solution().sortArrayByParity(nums))