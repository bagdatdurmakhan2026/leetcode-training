class Solution(object):
    def rotateRight(self, head, k):
        l = 0 
        r = len(head)
        arr = []
        for i in range(r):
            arr.pop(k)
            arr.insert(0,arr)
        return arr
            
        
head = [1,2,3,4,5]
k = 2
print(Solution().rotateRight(head, k))