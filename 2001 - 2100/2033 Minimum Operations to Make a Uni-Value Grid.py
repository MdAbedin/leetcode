class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = list(chain(*grid))
        m = sorted(nums)[len(nums)//2]

        return -1 if any(abs(num-m)%x != 0 for num in nums) else sum(abs(num-m)//x for num in nums)
