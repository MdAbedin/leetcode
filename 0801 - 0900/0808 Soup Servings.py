class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4451: return 1

        @cache
        def solve(n1,n2):
            if n1 <= 0 and n2 <= 0: return 0.5
            if n1 <= 0: return 1
            if n2 <= 0: return 0
            return (solve(n1-100,n2)+solve(n1-75,n2-25)+solve(n1-50,n2-50)+solve(n1-25,n2-75))/4

        return solve(n,n)
