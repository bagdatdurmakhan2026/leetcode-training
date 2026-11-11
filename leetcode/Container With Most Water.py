class Solution(object):
    def maxArea(self, height):
        ln = len(height)
        l = 0
        r = ln-1
        mx = 0
        while l < r:
            w = r - l
            cr = min(height[l], height[r])*w
            mx = max(mx, cr)
            if height[l]<height[r]:
                l+=1
            else: r-=1
        return mx   
height =[1,8,6,2,5,4,8,3,7]
ans = Solution()
print(ans.maxArea(height))      
