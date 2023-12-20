class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        return money if (ans := money-sum(sorted(prices)[:2])) < 0 else ans
