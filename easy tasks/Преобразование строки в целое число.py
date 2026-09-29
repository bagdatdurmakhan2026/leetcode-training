class Solution(object):
    def myAtoi(self, s):
        ans = "".join(char for char in s if  char.isalnum())
        return s     
s = "42 2 words"
print(Solution().myAtoi(s))
        