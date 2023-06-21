class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums_and_counts = list(Counter(candidates).items())

        @cache
        def solve(i,s):
            if i == len(nums_and_counts): return [[]] if s == 0 else []            
            return solve(i+1,s) + [[nums_and_counts[i][0]]*count + ans2 for count in range(1,nums_and_counts[i][1]+1) for ans2 in solve(i+1,s-nums_and_counts[i][0]*count)]

        return solve(0,target)
