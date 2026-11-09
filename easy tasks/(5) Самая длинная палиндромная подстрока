class Solution(object):
    def ans(self, s):
        n = len(s)
        start = 0
        mx = 0
        for i in range(n):
            l = i
            r = i
            while l>=0 and r<n and s[l]==s[r]:
                if r-l+1>mx:
                    mx = r-l+1
                    start = l
                l-=1
                r+=1
            l = i
            r = i+1
            while l>=0 and r<n and s[l]==s[r]:
                if r-l+1>mx:
                    mx = r-l+1
                    start = l
                l-=1
                r+=1      
s = "babadab"
print(Solution().ans(s))