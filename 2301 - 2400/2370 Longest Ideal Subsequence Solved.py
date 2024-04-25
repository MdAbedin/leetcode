class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        return max(reduce(lambda dp,c: [dp.__setitem__(ord(c)-ord("a"),max(dp[i] for i in range(len(dp)) if abs(i-(ord(c)-ord("a"))) <= k)+1),dp][1], s, [0]*26))
