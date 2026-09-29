class Solution(object):
    def reverse(self, x):
        cnt = -1
        if x > 0:
            ans = int(str(x)[::-1])
        elif x<0:
            ans = int(str(abs(x))[::-1]) *cnt
        else:
            return 0
        if ans< -2**31 or ans > 2**31 -1:
            return 0
        return ans
            
        
        
        
        
        
        
        
        
    