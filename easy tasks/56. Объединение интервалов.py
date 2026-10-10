class Solution(object):
    def merge(self, intervals):
        intervals.sort(key = lambda  x:x[0])
        arr = [intervals[0]]
        for i in intervals[1:]:
            last = arr[-1]
            if i[0] <= last[1]:
                last[1]= max(last[1], i[1])
            else:
                arr.append(i)
        return arr