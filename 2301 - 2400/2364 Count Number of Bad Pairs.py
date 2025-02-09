class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        counts = Counter()
        ans = 0

        for i,num in enumerate(nums):
            ans += i-counts[i-num]
            counts[i-num] += 1

        return ans
