class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        d = sum(num-nums[0] for num in nums)
        ans = [d]

        for i,(num1,num2) in enumerate(pairwise(nums)):
            d += (num2-num1)*(i+1)
            d -= (num2-num1)*(len(nums)-i-1)
            ans.append(d)

        return ans
