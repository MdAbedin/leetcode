class Solution:
    def maxDepth(self, s: str) -> int:
        return max(accumulate((c=="(")-(c==")") for c in s))
