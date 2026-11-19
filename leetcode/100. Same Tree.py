class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if (not p or not q) or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # 1. Базовый случай: оба узла None
        
        # 2. Базовый случай: один из узлов None или значения не равны
        
        # 3. Рекурсивно проверяем левых и правых потомков через and