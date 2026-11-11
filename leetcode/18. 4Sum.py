class Solution(object):
    def fourSum(self, nums, target):
        #l = 0
        n = len(nums)
        arr = []
        newN = sorted(enumerate(nums), key=lambda x:x[1])
        #curs = newN[0][1] + newN[1][1]+newN[2][1]+newN[3][1]
        if n < 4 :
            return []
        for i in range(n-3):
            if i > 0 and newN[i][1] == newN[i-1][1]:
                continue
            for j in range(i+1, n-2):
                if j> i+1 and newN[j][1] == newN[j-1][1]:
                    continue
                l = j+1
                r = n-1
                while l<r:
                    curv = newN[i][1] + newN[j][1]+newN[l][1]+newN[r][1]
                    if curv == target:
                        arr.append([newN[i][1],newN[j][1],newN[l][1],newN[r][1]])
                        l+=1
                        r-=1
                        while l<r and newN[l][1] == newN[l - 1][1]:
                            l+=1
                        while l < r and newN[r][1] == newN[r + 1][1]:
                            r -= 1
                    elif curv > target:
                            r-=1
                    else:
                            l+=1
        return arr
nums = [1,0,-1,0,-2,2]
target = 0
print(Solution().res(nums,target))

