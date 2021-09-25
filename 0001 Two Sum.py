# https://leetcode.com/problems/two-sum/

# brute force
# O(n^2) time | O(1) space
# Brute Force -- O(n^2) time | O(1) space
def twoSum(array, targetSum):
	for i in range(len(array) - 1):
		first_num = array[i]
		for j in range(i + 1, len(array)):
			second_num = array[j]
			if first_num + second_num == targetSum:
				return [first_num, second_num]
	return []

# Two-pass Hash Table
# O(n) time | O(n) space
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]] 

# One-pass Hash Table
# O(n) time | O(n) space

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # x + y = target
        # nested for loops
        seen = {}
        # loop nums 
        for i in range(len(nums)):
            complement = target - nums[i]
            # check if nums[i] is in seen, use  y = target - x
            if complement in seen:
                return [seen[complement], i]
            # if not --> add it to seen
            else:
                seen[nums[i]] = i 