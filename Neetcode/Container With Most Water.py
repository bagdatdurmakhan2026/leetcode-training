class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0 , len(heights)-1
        w = 0
        mx = 0
        while l < r :
            w = r - l
            cr = min(heights[l], heights[r]) * w
            mx = max(mx, cr)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return mx