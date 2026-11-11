class Solution(object):
    def removeDuplicates(self, nums):
        l = 0
        cnt=0
        r = len(nums) -1 
        while l <= r :
            if (l==0 or nums[l]!=nums[l-1]) and (l==r or nums[l]!=nums[l+1]):
                nums[cnt] = nums[l]
                cnt +=1
            l+=1
        del nums[cnt:]
        return nums     
nums = [1,2,3,3,4,4,5]

ans = Solution()
nas = ans.removeDuplicates(nums)
print(nas)