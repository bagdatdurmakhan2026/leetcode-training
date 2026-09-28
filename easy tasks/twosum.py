class Solution(object):
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    def r(self):
        for i in range(len(self.nums)):
            for j in range(i+1,len(self.nums)):
                if self.nums[j]==self.target-self.nums[i]:
                    return(i,j)
nums=[int(x) for x in input().split(",")]
target = int(input())
result = Solution(nums, target)
s = result.r()
print(s)