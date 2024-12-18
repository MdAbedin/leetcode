class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        return [p-next((p2 for p2 in prices[i+1:] if p2 <= p),0) for i,p in enumerate(prices)]
