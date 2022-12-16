class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counts = Counter(s)
        t_counts = Counter(t)

        return len(t) - sum(min(t_counts.get(char,0), count) for char, count in s_counts.items())
