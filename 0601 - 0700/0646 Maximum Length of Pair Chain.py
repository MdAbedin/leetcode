class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        prev_end = -inf
        ans = 0

        for l,r in sorted(pairs,key = lambda pair: pair[1]):
            if l > prev_end:
                ans += 1
                prev_end = r
            
        return ans
