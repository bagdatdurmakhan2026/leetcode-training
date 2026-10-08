class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        cnt1 = 1
        cnt2 = 1
        if not nums:
            return 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1]+1:
                cnt1+=1
            else:
                cnt2 =max(cnt2, cnt1)
                cnt1 =1 
        return max(cnt2,cnt1)
