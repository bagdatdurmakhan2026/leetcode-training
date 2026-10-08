#Интуиция и Идея решения
#from typing import List
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        arr = [intervals[0]]
        for i in intervals[1:]:
            last = arr[-1]
            if i[0] <=last[1]:
                last[1] = max(last[1], i[1])
            else:
                arr.append(i)
        return arr
# Проверка
sol = Solution()
print(sol.merge([[1, 3], [2, 6], [6, 10], [10, 18]]))