class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ans = 0

        for l in range(1,len(nums)+1):
            for ss in combinations(nums,l):
                s = set(ss)
                ans += all(x+k not in s and x-k not in s for x in s)

        return ans
