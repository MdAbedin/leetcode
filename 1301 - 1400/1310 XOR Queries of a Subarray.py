class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        px = list(accumulate([0]+arr,xor))
        return [px[r+1]^px[l] for l,r in queries]
