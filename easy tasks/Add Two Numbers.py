# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# # 
# # self.next = next
# import pandas as pd
# class Solution(object): 
#     def __init__(self, sa, da):
#         self.s = ""
#         self.v = ""
#         self.ass=sa
#         self.add=da
#     def r(self):
#         for num in self.ass:
#             self.s+=str(num)
#         for mun in self.add:
#             self.v+=str(mun)
#         result = int(self.s)
#         result2= int(self.v)
#         total = result+ result2
#         return total                                     
# sa = [int(c) for c in input().split(",")]
# da = [int(s) for s in input().split(",")]
# ta = Solution(sa, da)
# ruc = ta.r()
# ans = int(str(ruc)[::-1])
# print(ans)

# l1 = [2,4,3], l2 = [5,6,4] = [7,0,8]
#l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] #[8,9,9,9,0,0,0,1]
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Полный рабочий код но требует через NOde как изучу node вернусь с поиском решений проблемы
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         s =""
#         v=""
#         for i in l1:
#             s+=str(i)
#         for j in l2:
#             v+=str(j)
#         res = int(s)
#         res2 = int(v)
#         total = res+res2
#         return [int(g) for g in str(total)[::-1]]
# l1 = [9,9,9,9,9,9,9]
# l2 = [9,9,9,9]
# ta = Solution().addTwoNumbers(l1,l2)
# #ans = int(str(ta)[::-1])
# #
# #gg = [int(d) for d in str(ans)]
# print(ta)      

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        res = 0
        res2=0
        self.head = l1
        self.head2 = l2
        cur = self.head
        ruc = self.head2
        while cur is not None:
            res = res *10 + cur.val
            cur = cur.next
        while ruc is not None:
            res2 = res2 *10 + ruc.val
            ruc = ruc.next
        fn = res + res2
        return fn
l1 = [2,4,3]
l2 = [5,6,4]
jj  = Solution().addTwoNumbers(l1,l2)
print(jj)
    
        


        