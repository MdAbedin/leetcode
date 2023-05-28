class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        
        @cache
        def solve(l,r):
            return 0 if l > r else (cuts[r+1] if r+1 < len(cuts) else n)-(cuts[l-1] if l-1 >= 0 else 0) + min(solve(l,i-1)+solve(i+1,r) for i in range(l,r+1))

        return solve(0,len(cuts)-1)
