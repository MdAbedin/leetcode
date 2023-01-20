class Solution:
    """
    N = length of nums
    Time:  O(2^N * N)
    Space: O(2^N * N)
    """
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        for size in range(2, len(nums)+1):
            for subset in combinations(nums, size):
                if all(num1 <= num2 for num1,num2 in zip(subset,subset[1:])):
                    ans.add(subset)
                
        return ans
