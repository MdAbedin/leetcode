class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        ans = 0
        
        for char in s:
            balance += 1 if char == 'L' else -1
            
            if not balance: ans += 1
                
        return ans
