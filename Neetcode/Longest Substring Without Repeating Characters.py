class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = {}
        l, mx = 0,0
        for i, j in enumerate(s):
            if j in check and check[j] >= l:
                l = check[j]+1
            check[j] = i
            mx = max(mx, i-l+1)
        return mx
        