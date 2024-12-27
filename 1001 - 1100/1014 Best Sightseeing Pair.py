class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        m = ans = -inf

        for i,v in enumerate(values):
            ans = max(ans,v+m-i)
            m = max(m,v+i)

        return ans
