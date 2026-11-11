class Solution(object):
    def ans(self, nums, target):
        if target not in nums:
            return -1 
        l,r = 0, len(nums)-1
        while l <= r:
            if nums[l] == target:
                return l
            l+=1
        return []
    
nums = [4,5,6,7,0,1,2]
target = 0
print(Solution().ans(nums,target))
