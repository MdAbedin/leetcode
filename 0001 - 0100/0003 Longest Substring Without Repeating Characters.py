class Solution:
    """
    N = length of s
    Time:  O(N)
    Space: O(1)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        
        for start_i in range(len(s)):
            seen = set()
            
            for i in range(start_i, len(s)):
                if s[i] in seen: break
                seen.add(s[i])
                
            ans = max(ans, len(seen))
            
        return ans
