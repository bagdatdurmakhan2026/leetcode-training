class Solution(object):
    def nextPermutation(self, nums):
        l = 0
        r = len(nums)-1
        flag = True
        while l < r :
            if l >0 and nums[l] < nums[r]:
                nums[l],nums[r] = nums[r],nums[l]
            elif nums[l] > nums[r]:
                nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1
        return nums
nums = [1,1,5]
print(Solution().nextPermutation(nums))