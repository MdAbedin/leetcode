class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        i_nums = []
        stack = []

        for k,num in enumerate(nums):
            while stack and stack[-1][0] <= num: stack.pop()
            if (index := bisect_right(i_nums,(-num,inf))) < len(i_nums) and stack and i_nums[index][1] < stack[-1][1]: return True
            stack.append((num,k))
            if not i_nums or num < -i_nums[-1][0]: i_nums.append((-num,k))

        return False
