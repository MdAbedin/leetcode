class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return any(a&b&c&1 for a,b,c in zip(arr,arr[1:],arr[2:]))
