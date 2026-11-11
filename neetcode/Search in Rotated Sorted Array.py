class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums)-1
        new = sorted(enumerate(nums), key = lambda x:x[1])
        while l <= r :
            mid = (l+r)//2
            if new[mid][1] == target:
                return new[mid][0]
            if new[mid][1] > target:
                r =  mid -1
            else:
                l = mid + 1
        return -1
