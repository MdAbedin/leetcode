class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        
        while i < len(s)-1:
          if abs(ord(s[i]) - ord(s[i+1])) == abs(ord('a') - ord('A')):
            s = s[:i] + s[i+2:]
            i = 0
          else:
            i += 1
            
        return s
