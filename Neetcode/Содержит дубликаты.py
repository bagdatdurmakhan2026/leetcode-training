class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

nums = [1, 2, 3, 4]
print(Solution.hasDuplicate(nums))