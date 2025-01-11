class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return sum(c%2 for c in Counter(s).values()) <= k and len(s) >= k
