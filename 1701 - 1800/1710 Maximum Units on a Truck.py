class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        ans = 0
        
        for i in range(len(boxTypes)):
            g = min(boxTypes[i][0], truckSize)
            ans += g*boxTypes[i][1]
            truckSize -= g
            if not truckSize: break
            
        return ans
