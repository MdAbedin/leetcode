class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def solve(nums):
            if not nums: return 0,0

            l_score2,l_score1 = solve(nums[1:])
            l_score1 += nums[0]

            r_score2,r_score1 = solve(nums[:-1])
            r_score1 += nums[-1]

            return (l_score1,l_score2) if l_score1 >= r_score1 else (r_score1,r_score2)

        score1,score2 = solve(nums)

        return score1 >= score2
