class Solution:
    def minimumLength(self, s: str) -> int:
        return sum([2,1][c%2] for c in Counter(s).values())
