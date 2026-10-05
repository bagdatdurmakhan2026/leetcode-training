class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        l = 0
        cnt = 0
        r = len(people)-1
        while l<=r:
            if people[l] + people[r] <= limit:
                l+=1
            r-=1
            cnt+=1
        return cnt
        
people = [3,2,2,1]
limit =  3
print(Solution().numRescueBoats(people,limit))