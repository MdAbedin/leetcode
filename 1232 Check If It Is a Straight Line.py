class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1,y1 = coordinates[0]
        x2,y2 = coordinates[1]
        
        if x2 == x1:
            return all(x == x1 for x,y in coordinates)
        
        m = (y2-y1)/(x2-x1)
        b = y1 - m*x1
        
        for x,y in coordinates:
            if y != m*x + b:
                return False
            
        return True
