class Solution(object):
    def isPowerOfTwo(self, n):
        return True if (n&(n-1))==0 and n>0 else False 
n = 1
        