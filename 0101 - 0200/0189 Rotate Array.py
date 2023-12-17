class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(gcd(len(nums),k)):
            num = nums[i]
            
            for swap in range(len(nums)//gcd(len(nums),k)):
                i = (i+k)%len(nums)
                num,nums[i] = nums[i],num
