class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ans,cur = 0,0

        for i,(c,g) in enumerate(zip(customers,grumpy)):
            cur += g*c
            ans = max(ans,cur)
            if i-minutes+1 >= 0: cur -= grumpy[i-minutes+1]*customers[i-minutes+1]

        return ans + sum((1-g)*c for c,g in zip(customers,grumpy))
