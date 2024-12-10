class Solution:
    def maximumLength(self, s: str) -> int:
        return max((l for c in ascii_lowercase for l in range(1,s.count(c)+1) if len(re.findall(f'(?={c*l})',s)) >= 3),default=-1)
