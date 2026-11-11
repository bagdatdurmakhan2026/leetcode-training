class Solution(object):
    def searchInsert(self, nums, target):
        l,r = 0, len(nums)-1
        if target in nums:
            while l<=r:
                mid = (r+l)//2
                if nums[mid] == target:
                    return mid
                if nums[mid]>target:
                    r = mid-1
                else:
                    l = mid+1
        else:
            arr = list(nums)
            arr.append(target)
            arr.sort()
            i = 0
            j = len(arr)-1
            while i<=j:
                dim = (i+j)//2
                if nums[dim] == target:
                    return dim
                if nums[dim]>target:
                    r = dim-1
                else:
                    l = dim+1  
        return l
        """
# """
# class Solution(object):
#     def searchInsert(self, nums, target):
#         l, r = 0, len(nums) - 1
        
#         while l <= r:
#             mid = (l + r) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] > target:
#                 r = mid - 1
#             else:
#                 l = mid + 1
                
#         # Если цикл завершился и мы ничего не нашли, 
#         # переменная l — это и есть точный индекс для вставки!
#         return l
# """
        