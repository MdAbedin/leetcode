class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        lens = defaultdict(int)
        ans = 0
        
        for num in arr:
            lens[num] = lens[num-difference]+1
            ans = max(ans, lens[num])
            
        return ans
