class Solution(object):
    def ans(self, nums,k ):
        n = len(nums)
        k%=n
        arr = [0] * n
        for i in range(n):
            arr[(i+k)%n] = nums[i]
        nums[:] = arr
        return nums
        

nums = [1,2,3,4,5,6,7]
k = 3
print(Solution().ans(nums,k))