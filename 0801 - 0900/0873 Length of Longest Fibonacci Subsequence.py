class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nums = set(arr)
        ans = 0

        for num1,num2 in combinations(arr,2):
            l = 2

            while num1+num2 in nums:
                num1,num2 = num2,num1+num2
                l += 1

            if l >= 3: ans = max(ans,l)

        return ans
