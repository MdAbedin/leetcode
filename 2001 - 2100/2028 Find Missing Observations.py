class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        s = mean*(n+len(rolls)) - sum(rolls)
        if s not in range(n,6*n+1): return []

        ans = []

        for i in range(n):
            use = min(6,s-(n-i-1))
            ans.append(use)
            s -= use

        return ans
