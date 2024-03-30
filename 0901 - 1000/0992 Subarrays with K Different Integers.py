class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        r1 = r2 = ans = 0
        c1,c2 = Counter(),Counter()

        for l in range(len(nums)):
            while r1 < len(nums) and len(c1) < k:
                c1[nums[r1]] += 1
                r1 += 1

            while r2 < len(nums) and not(len(c2) == k and nums[r2] not in c2):
                c2[nums[r2]] += 1
                r2 += 1

            if len(c1) == k: ans += r2-r1+1
            
            c1[nums[l]] -= 1
            c2[nums[l]] -= 1
            if c1[nums[l]] == 0: c1.pop(nums[l])
            if c2[nums[l]] == 0: c2.pop(nums[l])

        return ans
