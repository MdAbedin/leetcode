class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum(abs(c1-c2) for c1,c2 in zip(Counter(ascii_lowercase+s).values(),Counter(ascii_lowercase+t).values()))//2
