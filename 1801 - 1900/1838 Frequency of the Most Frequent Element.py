class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        psums = [0]+list(accumulate(nums))
        return max(i-(bisect_left(range(i+1),0,key = lambda i2: k - (num*(i-i2+1) - (psums[i+1]-psums[i2]))))+1 for i,num in enumerate(nums))
