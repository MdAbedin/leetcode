class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stones_set = set(stones)

        @cache
        def solve(stone,prev_jump_len):
            if stone == stones[-1]: return True
            if stone not in stones_set: return False
            return any(solve(stone+jump_len,jump_len) for jump_len in (prev_jump_len-1,prev_jump_len,prev_jump_len+1) if jump_len >= 1)

        return solve(0,0)
