# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        l = range(head)
        for i in l-1:
            head[i],head[i+1]= head[i+1],head[i]
            break
        return head[i]