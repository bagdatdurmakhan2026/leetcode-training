class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height)-1
        mx = 0
        while l < r:
            w = r - l
            cr = min(height[l], height[r])*w
            mx = max(mx, cr)
            if height[l]<height[r]:
                l+=1
            else: r-=1
        return mx  