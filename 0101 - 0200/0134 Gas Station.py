class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans, gas_needed = len(gas)-1, 0
        
        for i in range(len(gas)-1,-1,-1):
            if gas[i]-cost[i] >= max(0,gas_needed): ans = i
            gas_needed += cost[i]-gas[i]
            gas_needed = max(gas_needed, cost[i]-gas[i])
            
        tank = 0
        for i in range(len(gas)):
            ind = (ans+i)%len(gas)
            tank += gas[ind]-cost[ind]
            if tank < 0: return -1
        
        return ans
