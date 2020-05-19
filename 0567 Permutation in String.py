class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = [s1.count(chr(ord('a') + i)) for i in range(26)]
        counts2 = [s2[:len(s1)].count(chr(ord('a') + i)) for i in range(26)]
        ans = counts2 == counts1
        if ans: return True
        
        for i in range(1,len(s2)-len(s1)+1):
            counts2[ord(s2[i-1]) - ord('a')] -= 1
            counts2[ord(s2[i+len(s1)-1]) - ord('a')] += 1
            
            if counts2 == counts1: return True
                
        return False
