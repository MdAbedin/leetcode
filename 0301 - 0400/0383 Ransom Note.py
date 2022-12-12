class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rcounts, mcounts = defaultdict(int), defaultdict(int)
        
        for char in ransomNote:
            rcounts[char] += 1
            
        for char in magazine:
            mcounts[char] += 1
            
        for char in ransomNote:
            if rcounts[char] > mcounts[char]:
                return False
            
        return True
