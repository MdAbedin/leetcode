class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        queen_locs = {tuple(queen) for queen in queens}
        
        for dy, dx in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]:
            cy, cx = king
            
            while cy >= 0 and cy < 8 and cx >= 0 and cx < 8:
                if (cy,cx) in queen_locs:
                    ans.append((cy,cx))
                    break
                    
                cy += dy
                cx += dx
                
        return ans
