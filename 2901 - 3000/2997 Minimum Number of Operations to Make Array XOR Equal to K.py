class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(reduce(xor,[num&(1<<i) for num in nums]) != k&(1<<i) for i in range(20))
