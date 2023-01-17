class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        left_ones, right_zeros = 0, s.count("0")
        ans = left_ones + right_zeros
        
        for c in s:
            if c == "0": right_zeros -= 1
            else: left_ones += 1
                
            ans = min(ans, left_ones + right_zeros)
        
        return ans
