class Solution:
    def clearDigits(self, s: str) -> str:
        while any(map(str.isdigit,s)):
            i = next(i for i,c in enumerate(s) if c.isdigit())
            i2 = [i2 for i2,c in enumerate(s[:i]) if not c.isdigit()][-1]
            s = "".join(c for i3,c in enumerate(s) if i3 not in [i,i2])
            
        return s
