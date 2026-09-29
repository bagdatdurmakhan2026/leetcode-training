class Solution(object):
    def isValid(self, s):
        ans={
            ")": "(","]" :"[","}":"{"
        }
        arr= []
        for char in s:
            if char in ans:
                tp=arr.pop() if arr else "#"
                if ans[char]!=tp:
                    return False
            else:   arr.append(char)
        return not arr      
