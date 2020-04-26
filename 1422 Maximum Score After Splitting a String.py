class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        s = [int(c) for c in s]
        total = sum(x for x in s)
        
        for i in range(len(s)):
            s[i] += s[i-1] if i-1 >= 0 else 0
            
        for i in range(len(s)-1):
            score = i+1-s[i] + total - s[i]
            max_score = max(max_score, score)
            
        return max_score
