class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        left_pad = 0
        
        for pair in shift:
            left_pad += pair[1] if pair[0] == 1 else -1*pair[1]

        left_pad %= len(s)
        return s[len(s)-left_pad:] + s[:len(s)-left_pad]
