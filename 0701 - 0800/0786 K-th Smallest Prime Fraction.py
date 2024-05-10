class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        return sorted(combinations(arr,2),key=lambda p: p[0]/p[1])[k-1]
