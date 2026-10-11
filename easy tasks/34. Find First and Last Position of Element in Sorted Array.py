class Solution(object):
    def searchRange(self, nums, target):
        def findBound(is_first):
            n = len(nums)-1
            l=0
            ans = -1
            while l <=n:
                mid = (n+l)//2
                if nums[mid] == target:
                    ans = mid
                    if is_first:
                        n = mid -1
                    else:
                        l = mid+1
                elif nums[mid] > target:
                    n = mid-1
                else:
                    l = mid + 1
            return ans
        return [findBound(True), findBound(False)] 
        