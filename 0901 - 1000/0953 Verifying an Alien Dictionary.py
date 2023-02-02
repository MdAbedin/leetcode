class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return sorted(words, key = lambda word: list(map(order.find, word))) == words
