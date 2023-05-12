class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def solve(i): return 0 if i >= len(questions) else max(questions[i][0] + solve(i+questions[i][1]+1), solve(i+1))
        return solve(0)
