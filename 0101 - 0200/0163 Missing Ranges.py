class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ans = []
        next_num = lower

        for num in nums:
            if num != next_num: ans.append([next_num,num-1])
            next_num = num+1

        if next_num <= upper: ans.append([next_num,upper])

        return ans
