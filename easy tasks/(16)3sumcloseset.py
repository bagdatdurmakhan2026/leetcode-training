class Solution(object):
    def threeSumClosest(self, nums, target):
        newN = sorted(enumerate(nums), key=lambda x:x[1])
        l = 0
        n = len(nums)
        avg = 0
        abc = newN[0][1]+newN[1][1]+newN[2][1]
        for i in range(n- 2):
            l = i+1
            r = n-1
            while l<r:
                curs = newN[i][1]+newN[l][1]+newN[r][1]
                if abs(curs-target) < abs(abc - target):
                    abc = curs
                if curs > target:
                    r-=1
                elif curs < target:
                    l+=1
                else:
                    return target      
        return abc
nums = [-1,2,-1,-4]
target = 1
print(Solution().threeSumClosest(nums,target))