# class Solution(object):
#     def removeElement(self, nums, val):
#         l = 0
#         r = 0
#         cnt = 0
#         n = len(nums)
#         while r < n:
#             if nums[l] == val:
#                 nums.pop(l)
#                 nums.append("_")
#             else:
#                 l+=1
#             r+=1
#         return f'{l},nums = [{",".join(map(str, nums))}]'
# nums = [0,1,2,2,3,0,4,2]
# val = 2
# print(Solution().removeElement(nums,val))

class Solution(object):
    def removeElement(self, nums, val):
        l = 0
        r = len(nums)-1 
        while l <= r:
            if nums[l]== val:
                nums[l]= nums[r]
                r-=1
            else:
                l+=1
        for i in range(l,len(nums)):
            nums[i]="_"
        return  f'{l}, [{",".join(map(str,nums))}]'
nums = [3,2,2,3]
val = 3
print(Solution().removeElement(nums,val))