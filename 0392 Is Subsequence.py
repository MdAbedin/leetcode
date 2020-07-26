class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        
        i, remaining = 0, len(s)
        
        for char in t:
            if char == s[i]:
                remaining -= 1
                i += 1
            if not remaining: return True
                
        return False
