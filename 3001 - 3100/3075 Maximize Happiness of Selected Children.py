class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        return sum(max(0,h-i) for i,h in enumerate(sorted(happiness,reverse=True)[:k]))
