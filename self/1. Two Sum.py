class Solution(object):
    def twoSum(self, nums, target):
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