class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = m = i = 0

        for i2,x in enumerate(arr):
            m = max(m,x)
            
            if i2-i == m-i:
                ans += 1
                i = i2+1
                m = 0

        return ans
