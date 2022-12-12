class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: max(x)-min(x), reverse=True)
        counts = [0,0]
        ans = 0
        
        for prices in costs:
            city = 0
            if prices[1] < prices[0]: city = 1
            if counts[city] == len(costs)/2: city = 1-city
            
            counts[city] += 1
            ans += prices[city]
            
        return ans
