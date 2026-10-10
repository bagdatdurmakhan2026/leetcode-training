class Solution(object):
    def merge(self, intervals,newInterval):
        t = intervals + [newInterval]
        t.sort(key = lambda  x:x[0])
        arr = [t[0]]
        for i in t[1:]:
            last = arr[-1]
            if i[0] <= last[1]:
                last[1]= max(last[1], i[1])
            else:
                arr.append(i)
        return arr
intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(Solution().merge(intervals, newInterval))