class Solution:
    def numSteps(self, s: str) -> int:
        s2 = s.strip("0")
        ans = len(s)-len(s2)
        return ans if len(s2) == 1 else ans+2+(s2.count("1")-1)+s2.count("0")*2
