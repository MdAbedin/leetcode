class Solution:
    def customSortString(self, S: str, T: str) -> str:
        ans = ""
        
        char_counts = defaultdict(int)
        for char in T:
            char_counts[char] += 1
            
        for char in S:
            ans += char_counts[char]*char
            char_counts[char] = 0
            
        for char in char_counts:
            ans += char_counts[char]*char
            
        return ans
