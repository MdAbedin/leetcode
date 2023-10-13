class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        s1,s2 = 0,0

        for num in cost: s1,s2 = s2,min(s1,s2)+num
        
        return min(s1,s2)
