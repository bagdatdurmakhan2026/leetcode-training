class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i >0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r :
                t = nums[i] + nums[r]+nums[l]
                if t < 0:
                    l+=1
                elif t > 0:
                    r-=1
                else:
                    res.append([nums[i],nums[l], nums[r]])
                    while l < r and nums[l]==nums[l+1]:
                        l+=1
                    while l < r and nums[r] == nums[r-1]:
                        r-=1
                l+=1
                r-=1
        return res
