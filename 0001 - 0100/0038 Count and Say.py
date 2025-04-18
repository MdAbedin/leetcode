class Solution:
    def countAndSay(self, n: int) -> str:
        return "1" if n == 1 else "".join(str(len(list(g)))+k for k,g in groupby(self.countAndSay(n-1)))
