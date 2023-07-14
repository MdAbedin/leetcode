class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ans = defaultdict(int)
        for num in arr[::-1]: ans[num] = 1+ans[num+difference]
        return max(ans.values())
