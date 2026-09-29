class Solution(object):
    def convert(self, s, numRows):
        l = 0
        n = len(s)
        if numRows == 1 or numRows >=n:
            return s
        r=[''] *numRows
        step = 1
        for char in s:
            r[l] += char
            if l == 0:
                step = 1
            elif l == numRows - 1:
                step = - 1
            l +=step
        return "".join(r)   
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
#s = "PAYPALISHIRING"
#numRows = 3