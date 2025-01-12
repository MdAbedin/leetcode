class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2: return False
        
        m1,m2 = 0,0

        for c,b in zip(s,locked):
            if b == "0":
                m1 = max(0,m1-1)
                m2 += 1
            else:
                if c == "(":
                    m1 += 1
                    m2 += 1
                else:
                    if m2 == 0: return False
                    m1 = max(0,m1-1)
                    m2 -= 1

        return m1 == 0
