class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        sum_counts = defaultdict(int)
        sum_counts[0] = 1
        ans = cur_sum = 0

        for bit in A:
            cur_sum += bit
            ans += sum_counts[cur_sum-S]
            sum_counts[cur_sum] += 1
            
        return ans
