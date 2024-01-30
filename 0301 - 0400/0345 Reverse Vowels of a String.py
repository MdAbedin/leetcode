class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [c for c in s if c.lower() in "aeiou"]
        return "".join(vowels.pop() if c.lower() in "aeiou" else c for c in s)
