# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         nums3 = nums1 + nums2
#         l = 0
#         n = len(nums3)-1
#         r = 0
#         while r <= n :
#             if nums3[r]!=0:
#                 nums3[l], nums3[r] = nums3[r],nums3[l]
#                 l+=1
#             r +=1
#         del nums3[l:]
#         nums3.sort()
#         return nums3
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# print(Solution().merge( nums1, m, nums2, n))
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums3 = nums1[:m] + nums2[:n]
        l = 0
        n = len(nums3)-1
        while l < n:
            if (l ==0 or nums3[l] >= nums3[l-1]):
                l+=1
            else:
                nums3[l],nums3[l-1] =nums3[l-1],nums3[l]
                l-=1        
        return nums3
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(Solution().merge(nums1, m, nums2, n ))