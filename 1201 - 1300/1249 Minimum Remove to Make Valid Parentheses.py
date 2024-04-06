class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = list(s)
        opens = []

        for i,c in enumerate(s):
            if c == "(":
                opens.append(i)
            elif c == ")":
                if not opens: ans[i] = ""
                else: opens.pop()
        
        for i in opens: ans[i] = ""

        return "".join(ans)
