class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        return sorted(arr1,key = lambda x: [inf if x not in arr2 else arr2.index(x),x])
