class Solution(object):
    def removeDuplicates(self, nums):
        l = 1
        n = len(nums)
        r = 1
        while r < n:
            if nums[l] == nums[l-1]:
                nums.pop(l)
                nums.append("_")
            else:
                l+=1
            r+=1
        return "{}, nums = [{}]".format(l, ",".join(map(str, nums)))
nums = [1,1,2]
print(Solution().removeDuplicates(nums))    
        
        
        