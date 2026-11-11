# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
# My solutin and Sol from website
# class Solution(object):
#     def swapPairs(self, head):
#         l = len(head)
#         for i in range(0,l-1,2):
#             head[i],head[i+1]= head[i+1],head[i]
#         return head
# head = [1,2,3,4]
# ans = Solution()
# nas = ans.swapPairs(head)
# print(nas) 
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):     
        pl = ListNode(0)
        pl.next = head
        pr = pl
        while pr.next and pr.next.next:
            first = pr.next
            second = pr.next.next
            first.next = second.next
            second.next = first
            pr.next = second
            pr = first    
        return pl.next

