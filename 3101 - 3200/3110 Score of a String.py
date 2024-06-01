class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(map(abs,starmap(sub,map(partial(map,ord),pairwise(s)))))
