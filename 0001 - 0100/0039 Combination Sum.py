class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        @cache
        def solve(i,s):
            if i == len(candidates): return [[]] if s == 0 else []
            return [[candidates[i]]*count+ans2 for count in range(s//candidates[i]+1) for ans2 in solve(i+1,s-candidates[i]*count)]

        return solve(0,target)
