class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def match(i,j):
            if j == len(p): return i == len(s)

            if j+1 < len(p) and p[j+1] == "*":
                if match(i,j+2): return True
                
                for i2 in range(i,len(s)):
                    if p[j] in [".",s[i2]]:
                        if match(i2+1,j+2):
                            return True
                    else:
                        return False
            else:
                return i < len(s) and p[j] in [".",s[i]] and match(i+1,j+1)

        return match(0,0)
