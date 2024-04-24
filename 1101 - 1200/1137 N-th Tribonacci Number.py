class Solution:
    def tribonacci(self, n: int) -> int:
        nums = [1,0,0]
        for _ in range(n): nums = nums[1:]+[sum(nums)]
        return nums[-1]
