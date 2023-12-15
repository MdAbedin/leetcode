class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return next(iter({c for pair in paths for c in pair}-{c1 for c1,c2 in paths}))
