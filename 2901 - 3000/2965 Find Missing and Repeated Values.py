class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        cs = Counter(chain(*grid))
        l = sorted(range(1,len(grid)**2+1),key=cs.__getitem__)
        return [l[-1],l[0]]
