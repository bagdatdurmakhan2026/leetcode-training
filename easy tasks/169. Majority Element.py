class Solution:
    def ans(self, nums):
        cnt = {}
        major_cnt = len(nums)//2
        for i in nums:
            cnt[i] = cnt.get(i,0) + 1
            if cnt[i] > major_cnt:
                return i   
nums = [3,2,3]
print(Solution.ans(nums))