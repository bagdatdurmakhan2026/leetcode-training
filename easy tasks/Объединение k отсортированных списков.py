# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        arr=[]
        for i in lists:
            for j in i:
                arr.append(j)
        arr.sort()
        return arr

lists = [[1,4,5],[1,3,4],[2,6]]
ans = Solution()
lg = ans.mergeKLists(lists)
print(lg)