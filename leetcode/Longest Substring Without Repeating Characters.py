# def asd(s):
#     ch = set()
#     ml = 0
#     lf = 0
#     for r in range(len(s)):
#         while s[r] in ch:
#             ch.remove(s[lf])
#             lf+=1
#         ch.add(s[r])
#         ml = max(ml,r-lf+1)
#     return ml
# ss = str(input())
# ass= asd(ss)
# print(ass)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l,mx,r = 0,0,0
        lseen = {
        }
        lm = len(s)
        while r<lm:
            if s[r] in lseen and lseen[s[r]]>=l:
                l = lseen[s[r]]+1
            lseen[s[r]]=r
            mx = max(mx,r-l+1)
            r+=1
        return mx