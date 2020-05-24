class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        ans = count = sum([s[:k].count(vowel) for vowel in vowels])
        
        for i in range(k, len(s)):
            count += 1 if s[i] in vowels else 0
            count -= 1 if s[i-k] in vowels else 0
            ans = max(ans,count)
            
        return ans
