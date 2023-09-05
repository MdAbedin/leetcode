class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        tank = 0

        for i,g,c in zip(range(len(gas)),gas,cost):
            tank += g-c

            if tank < 0:
                tank = 0
                start = i+1

        tank = 0

        for i in range(len(gas)):
            tank += gas[(start+i)%len(gas)]-cost[(start+i)%len(cost)]
            if tank < 0: return -1

        return start
