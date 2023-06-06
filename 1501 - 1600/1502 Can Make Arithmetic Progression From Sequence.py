class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        return len({num2-num1 for num1,num2 in pairwise(sorted(arr))}) == 1
