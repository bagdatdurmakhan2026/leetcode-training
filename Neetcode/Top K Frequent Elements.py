from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr ={}
        for i in nums:
            arr[i] = arr.get(i,0) + 1
        res = [[] for _ in range(len(nums)+1)]
        for i,j in arr.items():
            res[j].append(i)
        ans = []
        for x in range(len(res)-1,0,-1):
            for i in res[x]:
                ans.append(i)
                if len(ans)==k:
                    return ans
        return ans
nums = [1,2,2,3,3,3]
k = 2
print(Solution.topKFrequent(nums, k))