class Solution(object):
    def lengthOfLastWord(self, s):
        text = s.split()
        lw = text[-1]
        nas = len(lw)
        return nas
        
        """
        :type s: str
        :rtype: int
        """
s = "Hello World"       