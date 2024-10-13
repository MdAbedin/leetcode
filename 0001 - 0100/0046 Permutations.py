class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]

        answers = []
        
        for i,num in enumerate(nums):
            remaining_perms = self.permute(nums[:i] + nums[i+1:])
            for remaining_perm in remaining_perms: answers.append([num]+remaining_perm)

        return answers
