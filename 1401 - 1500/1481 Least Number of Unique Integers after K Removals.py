class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        return len(set(arr))-bisect_right(list(accumulate(sorted(Counter(arr).values()))),k)
