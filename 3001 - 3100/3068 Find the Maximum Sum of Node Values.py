class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        if sum(num < num^k for num in nums)%2 == 0: return sum(max(num,num^k) for num in nums)
        else: return sum(max(num,num^k) for num in nums) - min(abs(num-(num^k)) for num in nums)
