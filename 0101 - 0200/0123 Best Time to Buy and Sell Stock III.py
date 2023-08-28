class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min1,min2 = inf,inf
        ans1,ans2 = 0,0

        for p in prices:
            ans1,ans2 = max(ans1,p-min1),max(ans2,p-min2)
            min1,min2 = min(min1,p),min(min2,p-ans1)

        return ans2
