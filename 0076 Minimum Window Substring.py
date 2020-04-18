class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            quit()
        if not s:
            return ""
        
        left = ans_left = 0
        right = -1
        ans_right = len(s)-1
        to_find = 0
        char_counts = defaultdict(int)
        
        for char in t:
            char_counts[char] += 1
            to_find += 1
        
        while right+1 < len(s):
            right += 1
            if s[right] in char_counts:
                to_find -= 1 if char_counts[s[right]] >= 1 else 0
                char_counts[s[right]] -= 1
            
            while to_find == 0 and (s[left] not in char_counts or char_counts[s[left]] < 0):
                if s[left] in char_counts:
                    char_counts[s[left]] += 1
                left += 1
                
            if to_find == 0 and right-left < ans_right-ans_left:
                ans_right = right
                ans_left = left
                
        return s[ans_left:ans_right+1] if to_find == 0 else ""
