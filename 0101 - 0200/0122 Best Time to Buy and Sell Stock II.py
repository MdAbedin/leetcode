class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0,price2-price1) for price1,price2 in pairwise(prices))
