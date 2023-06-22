class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        ans,best_buy = 0,-inf
        
        for price in prices: ans,best_buy = max(ans,best_buy+price-fee), max(best_buy,ans-price)

        return ans
