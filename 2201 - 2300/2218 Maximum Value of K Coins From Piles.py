class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @cache
        def helper(i,coins_left):
            if i == len(piles) or coins_left == 0: return 0

            ans = helper(i+1,coins_left)
            wallet = 0

            for j in range(len(piles[i])):
                wallet += piles[i][j]
                ans = max(ans, wallet + helper(i+1,coins_left-1))
                coins_left -= 1
                if coins_left == 0: break

            return ans

        return helper(0,k)
