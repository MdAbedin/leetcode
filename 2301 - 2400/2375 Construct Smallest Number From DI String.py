class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def solve(nums):
            if len(nums) == len(pattern)+1: return "".join(map(str,nums))

            for num in range(1,10):
                if num in nums or (nums and (num > nums[-1]) ^ (pattern[len(nums)-1] == "I")): continue
                if (ans := solve(nums+[num])): return ans

        return solve([])
