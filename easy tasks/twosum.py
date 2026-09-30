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


