class Solution(object):
    def minCut(self, s):
        if len(s)<=1: 
            return 0
        mx = 0
        n = len(s)
        arr = [i for i in range(n)]
        for i in range(n):
            l = i
            r = i 
            while l >= 0 and r < n and s[l] == s[r]:
                if l == 0:
                    arr[r] = 0
                else:
                    arr[r] = min(arr[r],arr[l-1]+1) 
                l-=1
                r+=1
            l = i
            r = i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if l == 0:
                    arr[r] = 0
                else:
                    arr[r] = min(arr[r],arr[l-1]+1) 
                l-=1
                r+=1
        return arr[n-1]              
s = "efe"
print(Solution().minCut(s))