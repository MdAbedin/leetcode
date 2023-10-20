class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        radix = 10
        exponent = 1
        nums2 = [0]*len(nums)

        for i in range(10):
            counts = [0]*radix
            for num in nums: counts[(num//exponent)%radix] += 1
            counts = list(accumulate(counts))
            
            for num in nums[::-1]:
                nums2[counts[(num//exponent)%radix]-1] = num
                counts[(num//exponent)%radix] -= 1

            nums = nums2[:]
            exponent *= radix

        return max((num2-num1 for num1,num2 in pairwise(nums)),default=0)
