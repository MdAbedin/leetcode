class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ps = [0]+list(accumulate({w[0],w[-1]} <= set("aeiou") for w in words))
        return [ps[r+1]-ps[l] for l,r in queries]
