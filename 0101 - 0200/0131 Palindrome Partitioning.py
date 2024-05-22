class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return [[s[i1:i2] for i1,i2 in pairwise([0,*ss,len(s)])] for l in range(len(s)) for ss in combinations(range(1,len(s)),l) if all(s2 == s2[::-1] for s2 in [s[i1:i2] for i1,i2 in pairwise([0,*ss,len(s)])])]
