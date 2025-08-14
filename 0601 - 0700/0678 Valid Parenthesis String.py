class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def solve(i,level):
            if i == len(s): return level == 0
            if level < 0: return False

            if s[i] == "(": return solve(i+1,level+1)
            if s[i] == ")": return solve(i+1,level-1)
            if s[i] == "*": return any(solve(i+1,level+x) for x in [-1,0,1])

        return solve(0,0)
