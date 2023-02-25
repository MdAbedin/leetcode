class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = inf
        ans = 0
        
        for price in prices:
            ans = max(ans, price - min_price)
            min_price = min(min_price, price)
            
        return ans
