class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        @cache
        def solve(i):
            if i == len(nums): return 0,1

            max_length = 0
            ans = 0

            for i2 in range(i+1,len(nums)+1):
                if i2 < len(nums) and nums[i] >= nums[i2]: continue

                max_length2,ans2 = solve(i2)
                max_length2 += 1

                if max_length2 > max_length:
                    max_length = max_length2
                    ans = ans2
                elif max_length2 == max_length:
                    ans += ans2

            return max_length,ans

        counts = Counter()
        for max_length,ans in map(solve,range(len(nums))): counts[max_length] += ans

        return counts[max(counts)]
