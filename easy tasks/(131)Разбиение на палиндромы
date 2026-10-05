class Solution(object):
    def partition(self, s):
        if not s: 
            return ""
        def check(l, r):
            while l <r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        l,r = 0, len(s)-1
        while l < r :
            if s[l]!=s[r]:
                return check(l+1,r) or check(l, r -1)
            l+=1
            r-=1
        return True
s = "aabc"
print(Solution().partition(s))