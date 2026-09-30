
class Solution(object):
    def removeDuplicates(self, nums):
        s = set()
        for i in nums:
            if i in s:
                nums.remove(i)
            else: s.add(i)
        return nums
nums = [0,0,1,1,1,2,2,3,3,4]

ans = Solution()
nas = ans.removeDuplicates(nums)
print(nas)