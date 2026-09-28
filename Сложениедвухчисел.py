# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
# 
# self.next = next
import pandas as pd
class Solution(object): 
    def __init__(self, sa, da):
        self.s = ""
        self.v = ""
        self.ass=sa
        self.add=da
    def r(self):
        for num in self.ass:
            self.s+=str(num)
        for mun in self.add:
            self.v+=str(mun)
        result = int(self.s)
        result2= int(self.v)
        total = result+ result2
        return total                                     
sa = [int(c) for c in input().split(",")]
da = [int(s) for s in input().split(",")]
ta = Solution(sa, da)
ruc = ta.r()
ans = int(str(ruc)[::-1])
print(ans)

# l1 = [2,4,3], l2 = [5,6,4] = [7,0,8]
#l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] #[8,9,9,9,0,0,0,1]




        