class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        ans = 0
        score = 0
        tokens.sort()
        l,r = 0,len(tokens)-1

        while l <= r:
            while l <= r and power-tokens[l] >= 0:
                power -= tokens[l]
                score += 1
                l += 1

            ans = max(ans,score)

            if score == 0: break

            if r >= l:
                score -= 1
                power += tokens[r]
                r -= 1

        return ans
