class Solution(object):
    def res(self, nums, target):
        rev = sorted(enumerate(nums), key= lambda x:x[1])
        l = 0
        r = len(nums)-1
        while l<r:
            if rev[l][1]+rev[r][1]==target:
                return [rev[l][0],rev[r][0]]
            if rev[l][1]+rev[r][1]>target:
                r-=1
            else:
                l+=1
        return []
nums = [1,2,4,3,7,5]
target = 5
print(Solution().res(nums,target))      
"""
class Solution(object):
    def twoSum(self, nums, target):
        l = len(nums)
        for i in range(0,l,1):
            for j in range(i+1,l,1):
                if nums[j]== target - nums[i]:
                    return [i,j]
        return []
nums=[int(x) for x in input().split(",")]
target = int(input())
result = Solution().twoSum(nums, target)
print(result)         
"""

