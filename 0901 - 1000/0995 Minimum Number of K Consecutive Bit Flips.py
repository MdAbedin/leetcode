class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        ends = set()
        flipped = False
        ans = 0

        for i in range(len(nums)):
            if not((nums[i] == 1) ^ flipped):
                if i > len(nums)-k: return -1
                ans += 1
                flipped = not flipped
                ends.add(i+k-1)

            if i in ends: flipped = not flipped

        return ans
