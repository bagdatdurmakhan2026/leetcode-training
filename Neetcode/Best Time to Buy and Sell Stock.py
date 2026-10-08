class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = float('inf')
        mx = 0
        for i in prices:
            if i < mn:
                mn = i
            elif i - mn> mx:
                mx = i - mn
        return mx
