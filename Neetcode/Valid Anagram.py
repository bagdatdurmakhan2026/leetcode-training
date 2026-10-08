class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt1 ={}
        cnt2= {}
        for i in s:
            cnt1[i] = cnt1.get(i,0)+1
        for j in t:
            cnt2[j] = cnt2.get(j,0)+1
        return  cnt1 == cnt2
s = "racecar"
t = "carrace"
print(Solution.isAnagram(s,t))