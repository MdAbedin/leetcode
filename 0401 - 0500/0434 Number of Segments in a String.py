class Solution:
    def countSegments(self, s: str) -> int:
        if not s: return 0
        return len(s.split())
