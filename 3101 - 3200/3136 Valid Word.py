class Solution:
    def isValid(self, word: str) -> bool:
        return bool(len(word) >= 3 and word.isalnum() and set("aeiou")&set(word.lower()) and set(word.lower())-set("aeiou")-set(digits))
