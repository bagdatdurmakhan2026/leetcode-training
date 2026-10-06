class Solution(object):
    def sortList(self, head):
        n = len(head)
        check = False
        while not check:
            check = True
            for i in (0,1):
                for j in range(i,n-1,2):
                    x = j+1
                    if head[j]> head[x]:
                        head[j],head[x] = head[x], head[j]
                        check = False
        return head
                        
head = [4,2,1,3]
print(Solution().sortList(head))