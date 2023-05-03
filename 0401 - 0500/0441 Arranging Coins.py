class Solution:
    def arrangeCoins(self, n: int) -> int:
        coins_used = 0
        complete_rows = 0

        while coins_used + complete_rows+1 <= n:
            coins_used += complete_rows+1
            complete_rows += 1

        return complete_rows
