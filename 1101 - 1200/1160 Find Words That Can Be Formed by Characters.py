class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        return sum(len(w) for w in words if Counter(w) <= Counter(chars))
