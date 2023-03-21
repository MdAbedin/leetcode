class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        streak = 0

        for num in nums:
            if num == 0: streak += 1
            else: streak = 0
            ans += streak

        return ans
