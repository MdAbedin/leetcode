class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        return sum(nums[i1] == nums[i2] and (i1*i2)%k == 0 for i1,i2 in combinations(range(len(nums)),2))
