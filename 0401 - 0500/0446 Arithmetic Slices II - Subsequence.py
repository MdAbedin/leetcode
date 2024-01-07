class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = []

        for i,num in enumerate(nums):
            cur_ans = defaultdict(int)

            for i2 in range(i):
                d = num-nums[i2]
                cur_ans[d] += dp[i2][d]+1

            dp.append(cur_ans)

        return sum(sum(d.values()) for d in dp) - comb(len(nums),2)
