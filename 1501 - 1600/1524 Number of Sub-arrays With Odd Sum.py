class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        counts = [1,0]
        s = 0
        ans = 0

        for num in arr:
            s += num
            ans += counts[1-s%2]
            counts[s%2] += 1

        return ans%(10**9+7)
