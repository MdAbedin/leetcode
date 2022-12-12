class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = sorted(cuts)
        cuts = [0] + cuts + [n]
        
        dp = [[float('inf')]*len(cuts) for _ in range(len(cuts))]
        
        for size in range(1, len(cuts)):
            for i in range(len(cuts)-size):
                if size == 1: dp[i][i+size] = 0
                else:
                    cost = cuts[i+size]-cuts[i]
                    for mid in range(i+1, i+size):
                        dp[i][i+size] = min(dp[i][i+size], cost + dp[i][mid] + dp[mid][i+size])
                        
        return dp[0][-1]
