class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [num for num,count in Counter(nums).items() if count > len(nums)//3]
