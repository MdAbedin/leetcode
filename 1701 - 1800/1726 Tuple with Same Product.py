class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counts = Counter(nums[i]*nums[j] for i in range(len(nums)) for j in range(i))
        ans = 0

        for i in range(len(nums)):
            for j in range(i):
                counts[nums[i] * nums[j]] -= 1
                ans += counts[nums[i]*nums[j]]

        return ans*8
