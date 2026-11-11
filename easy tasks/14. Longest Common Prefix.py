class Solution(object):
    def ans(self, s):
        n= len(s)
        for i in range(len(s[0])):
            char = s[0][i]
            for j in range(1,n):
                if i == len(s[j]) or s[j][i] != char:
                    return s[0][:i]
        return s[0]      
s = ["flower","flow","flight"]
print(Solution().ans(s))