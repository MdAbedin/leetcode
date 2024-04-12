class Solution:
    def trap(self, height: List[int]) -> int:
        l = []
        for h in height: l.append(max(0 if not l else l[-1],h))

        r = []
        for h in height[::-1]: r.append(max(0 if not r else r[-1],h))
        r.reverse()

        return sum(min(l,r)-h for l,r,h in zip(l,r,height))
