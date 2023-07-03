class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        diffs = [[c1,c2] for c1,c2 in zip(s,goal) if c1 != c2]
        return max(Counter(s).values()) >= 2 if not diffs else len(diffs) == 2 and diffs[0] == diffs[1][::-1]
