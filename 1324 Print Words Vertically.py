class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(' ')
        ans = []
        
        for i in range(max(len(word) for word in words)):
            ans.append(''.join(word[i] if i < len(word) else ' ' for word in words).rstrip())
            
        return ans
