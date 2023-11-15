class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        ans = 0
        for i,num in enumerate(sorted(arr)): ans = min(ans+1,num)
        return ans
