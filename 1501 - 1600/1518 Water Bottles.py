class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans,empty = 0,0

        while numBottles:
            ans += numBottles
            numBottles,empty = divmod(numBottles+empty,numExchange)
        
        return ans
