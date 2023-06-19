class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        return "".join(str(len(list(g)))+k for k,g in groupby(self.countAndSay(n-1)))
