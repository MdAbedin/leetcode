class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        ans = cur_ans = sum(map(mul,nums,cost))
        add,subtract = 0,sum(cost)
        prev = 0
        num_to_cost = Counter()
        for num,c in zip(nums,cost): num_to_cost[num] += c

        for num in sorted(set(nums)):
            cur_ans += (num-prev)*(add-subtract)
            ans = min(ans,cur_ans)
            add += num_to_cost[num]
            subtract -= num_to_cost[num]
            prev = num

        return ans
