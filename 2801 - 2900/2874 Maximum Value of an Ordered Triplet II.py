class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        m = -inf
        d = -inf
        ans = 0
        
        for num in nums:
            ans = max(ans,num*d)
            d = max(d,m-num)
            m = max(m,num)
        
        return ans
