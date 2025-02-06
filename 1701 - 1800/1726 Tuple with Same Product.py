class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counts = Counter()
        ans = 0

        for i1,i2 in combinations(range(len(nums)),2):
            ans += counts[nums[i1]*nums[i2]]
            counts[nums[i1]*nums[i2]] += 1

        return ans*8
