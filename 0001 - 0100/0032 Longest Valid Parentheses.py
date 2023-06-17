class Solution:
    def longestValidParentheses(self, s: str) -> int:
        level_starts = {}
        level = 0
        ans = 0

        for i,c in enumerate(s):
            if c == ")":
                level -= 1
                ans = max(ans,i-level_starts.get(level,inf)+1)
                level_starts.pop(level+1,None)

            if c == "(":
                if level not in level_starts: level_starts[level] = i
                level += 1

        return ans
