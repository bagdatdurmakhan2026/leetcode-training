class Solution(object):
    def isSymmetric(self, root):
        def isMirror(l, r):
            if not l and not r:
                return True
            if not l or not r or l.val != r.val:
                return False
            return isMirror(l.left, r.right) and isMirror(l.right, r.left)
        
        return isMirror(root.left, root.right)