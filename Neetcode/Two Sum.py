class Solution:
    def twoSum(self, nums, target):
        new = sorted(enumerate(nums), key = lambda x:x[1])
        l,r = 0, len(nums)-1
        while l < r :
            curs = new[l][1]+new[r][1]
            if curs==target:
                return sorted([new[l][0],new[r][0]])
            elif curs> target:
                r-=1
            else:
                l+=1
        return []
nums = [3,4,5,6]
target = 7
print(Solution.twoSum(nums ,target))