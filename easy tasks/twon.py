class Solution(object):
    def addTwoNumbers(self, l1, l2):
        s1 = "".join(str(x) for x in reversed(l1)) # 342
        s2 = "".join(str(y) for y in reversed(l2)) # 465 -> 807
        res = int(s1)+int(s2)
        arr = []
        while res>0:
            digit = res %10
            arr.append(digit)
            res//=10
        return arr

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
print(Solution().addTwoNumbers(l1,l2))