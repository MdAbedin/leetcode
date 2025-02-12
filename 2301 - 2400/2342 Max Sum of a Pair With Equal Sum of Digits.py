class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = defaultdict(lambda:-inf)
        ans = -1

        for num in nums:
            s = sum(map(int,str(num)))
            ans = max(ans,num+d[s])
            d[s] = max(d[s],num)

        return ans
