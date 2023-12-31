class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        inds = defaultdict(list)
        for i,c in enumerate(s): inds[c].append(i)
        return max([inds2[-1]-inds2[0]-1 for inds2 in inds.values()],default=-1)
