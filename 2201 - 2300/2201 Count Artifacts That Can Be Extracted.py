class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        digs = set(map(tuple,dig))
        return sum(all((r,c) in digs for r in range(a[0],a[2]+1) for c in range(a[1],a[3]+1)) for a in artifacts)
