class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counts = [p.count(chr(ord('a') + i)) for i in range(26)]
        s_counts = [s[:len(p)].count(chr(ord('a') + i)) for i in range(26)]
        ans = [0] if p_counts == s_counts else []
        
        for i in range(1, len(s)-len(p)+1):
            s_counts[ord(s[i-1]) - ord('a')] -= 1
            s_counts[ord(s[i+len(p)-1]) - ord('a')] += 1
            if s_counts == p_counts:
                ans.append(i)
        
        return ans
