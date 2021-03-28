class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = "".join([char if char.isdigit() else " " for char in word])
        return len({int(num) for num in s.split()})
        
