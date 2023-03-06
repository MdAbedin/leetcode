class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:

        arr = set(arr)

        return [num for num in range(1,2001) if num not in arr][k-1]
