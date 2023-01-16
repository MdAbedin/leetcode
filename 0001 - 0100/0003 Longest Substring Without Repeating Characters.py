class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        
        for start_i in range(len(s)):
            seen = set()
            
            for end_i in range(start_i, len(s)):
                if s[end_i] in seen: break
                seen.add(s[end_i])
                
            ans = max(ans, len(seen))
            
        return ans
